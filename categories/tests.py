from django.test import TestCase

from countries.models import Country

from .models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        # Create a sample country for testing
        country = Country.objects.create(
            name="Test Country", flag="https://example.com/flag.png", currency="USD"
        )

        # Create a sample category for testing
        Category.objects.create(
            country=country, title="Test Category", price_per_kilo=10.5
        )

    def test_category_country(self):
        # Retrieve the category created in the setup
        test_category = Category.objects.get(title="Test Category")
        self.assertEqual(test_category.country.name, "Test Country")

    def test_category_title(self):
        test_category = Category.objects.get(title="Test Category")
        self.assertEqual(test_category.title, "Test Category")

    def test_category_price_per_kilo(self):
        test_category = Category.objects.get(title="Test Category")
        self.assertEqual(test_category.price_per_kilo, 10.5)

    def test_category_str_method(self):
        test_category = Category.objects.get(title="Test Category")
        self.assertEqual(str(test_category), "Test Category")
