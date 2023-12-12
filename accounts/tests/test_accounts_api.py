from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class LoginAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="arter@tendean.com",
            email="arter@tendean.com",
            password="password",
        )
        self.url = reverse("accounts-api:login")

    def test_login_api_success(self):
        login_data = {"email": "arter@tendean.com", "password": "password"}
        response = self.client.post(self.url, login_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)

    def test_login_api_invalid_credentials(self):
        invalid_login_data = {"email": "arter@tendean.lol", "password": "wrongpassword"}
        response = self.client.post(self.url, invalid_login_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_api_user_not_found(self):
        non_existent_user_data = {
            "email": "nonexistent@example.com",
            "password": "password",
        }
        response = self.client.post(self.url, non_existent_user_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("There is no user with this email", response.data["email"])


class RegisterAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("accounts-api:register")
        self.valid_payload = {
            "email": "test@example.com",
            "password": "securepassword123",
        }

    def test_registration_successful(self):
        response = self.client.post(
            self.register_url, self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_registration_duplicate_email(self):
        User.objects.create_user(
            username=self.valid_payload["email"],
            email=self.valid_payload["email"],
            password=self.valid_payload["password"],
        )

        response = self.client.post(
            self.register_url, self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("already taken", str(response.data))

    def test_registration_weak_password(self):
        weak_password_payload = {"email": "test@example.com", "password": "weak"}

        response = self.client.post(
            self.register_url, weak_password_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Password must be at least 6 characters", str(response.data))
