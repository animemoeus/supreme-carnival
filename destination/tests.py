from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class CheckDestinationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("destination-api:index")

    def test_empty_params(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"message": "`search` params is required."})

    def test_after_params(self):
        response = self.client.get(self.url, {"search": "your_search_term"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data,
            {"message": "Your_search_term is not available for destination."},
        )

    def test_manado_params(self):
        response = self.client.get(self.url, {"search": "Manado"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {"message": "Manado is available for destination."}
        )
