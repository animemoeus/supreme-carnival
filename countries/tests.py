from django.test import TestCase

from .models import Country


class CountryModelTest(TestCase):
    def setUp(self):
        # Create a sample country for testing
        Country.objects.create(
            name="Test Country", flag="https://example.com/flag.png", currency="USD"
        )

    def test_country_name(self):
        # Retrieve the country created in the setup
        test_country = Country.objects.get(name="Test Country")
        self.assertEqual(test_country.name, "Test Country")

    def test_country_flag(self):
        test_country = Country.objects.get(name="Test Country")
        self.assertEqual(test_country.flag, "https://example.com/flag.png")

    def test_country_currency(self):
        test_country = Country.objects.get(name="Test Country")
        self.assertEqual(test_country.currency, "USD")

    def test_country_str_method(self):
        test_country = Country.objects.get(name="Test Country")
        self.assertEqual(str(test_country), "Test Country")
