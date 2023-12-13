from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from countries.models import Country


class CountryAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Country.objects.create(
            name="TestCountry", flag="http://example.com/flag.jpg", currency="TEST"
        )

    def test_country_list_api_view(self):
        url = reverse("countries-api:index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_country_search_api_view(self):
        url = reverse("countries-api:index")
        response = self.client.get(url, {"search": "TestCountry"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
