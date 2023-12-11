from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


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
