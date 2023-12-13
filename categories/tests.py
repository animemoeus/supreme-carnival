from django.test import TestCase
from django.urls import reverse

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


class CategoryViewsTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Test Country")
        self.category = Category.objects.create(
            country=self.country,
            title="Test Category",
            price_per_kilo=10.0,
        )

    def test_category_list_view(self):
        response = self.client.get(reverse("categories:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Category")

    def test_create_category_view(self):
        response = self.client.post(
            reverse("categories:create"),
            {
                "country": self.country.id,
                "title": "New Category",
                "price_per_kilo": 15.0,
            },
        )
        self.assertEqual(response.status_code, 302)
        new_category = Category.objects.get(title="New Category")
        self.assertEqual(new_category.price_per_kilo, 15.0)

    def test_update_category_view(self):
        response = self.client.post(
            reverse("categories:update", args=[self.category.id]),
            {
                "country": self.country.id,
                "title": "Updated Category",
                "price_per_kilo": 20.0,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.category.refresh_from_db()
        self.assertEqual(self.category.title, "Updated Category")
        self.assertEqual(self.category.price_per_kilo, 20.0)

    def test_delete_category_view(self):
        response = self.client.post(
            reverse("categories:delete", args=[self.category.id])
        )
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(pk=self.category.id)
