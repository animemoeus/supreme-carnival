from django.test import TestCase
from django.urls import reverse

from countries.models import Country


class CountryTests(TestCase):
    def setUp(self):
        self.test_country = Country.objects.create(
            name="TestCountry", flag="https://example.com/flag.png", currency="USD"
        )

    def test_country_list_view(self):
        response = self.client.get(reverse("countries:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.test_country.name)

    def test_country_create_view(self):
        response = self.client.post(
            reverse("countries:create"),
            {
                "name": "NewCountry",
                "flag": "https://example.com/new_flag.png",
                "currency": "EUR",
            },
        )
        self.assertEqual(response.status_code, 302)

        new_country = Country.objects.get(name="NewCountry")
        self.assertIsNotNone(new_country)

    def test_country_edit_view(self):
        response = self.client.post(
            reverse("countries:edit", args=[self.test_country.pk]),
            {
                "name": "UpdatedCountry",
                "flag": "https://example.com/updated_flag.png",
                "currency": "GBP",
            },
        )
        self.assertEqual(response.status_code, 302)

        updated_country = Country.objects.get(pk=self.test_country.pk)
        self.assertEqual(updated_country.name, "UpdatedCountry")

    def test_country_delete_view(self):
        response = self.client.post(
            reverse("countries:delete", args=[self.test_country.pk])
        )
        self.assertEqual(response.status_code, 302)

        with self.assertRaises(Country.DoesNotExist):
            Country.objects.get(pk=self.test_country.pk)
