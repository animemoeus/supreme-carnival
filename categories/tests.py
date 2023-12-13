from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category
from countries.models import Country

from .models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
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


class CategoryListAPITest(APITestCase):
    def setUp(self):
        self.country1 = Country.objects.create(
            name="Test Country 1", flag="https://example.com/flag1.png", currency="USD"
        )
        self.country2 = Country.objects.create(
            name="Test Country 2", flag="https://example.com/flag2.png", currency="EUR"
        )
        self.country3 = Country.objects.create(
            name="Test Country 3", flag="https://example.com/flag3.png", currency="GBP"
        )

        self.category1 = Category.objects.create(
            country=self.country1, title="Category 1", price_per_kilo=10.0
        )
        self.category2 = Category.objects.create(
            country=self.country1, title="Category 2", price_per_kilo=15.0
        )
        self.category3 = Category.objects.create(
            country=self.country2, title="Category 3", price_per_kilo=12.0
        )
        self.category4 = Category.objects.create(
            country=self.country2, title="Category 4", price_per_kilo=8.0
        )
        self.category5 = Category.objects.create(
            country=self.country3, title="Category 5", price_per_kilo=20.0
        )

    def test_category_list_api_view_with_search_and_filter(self):
        url = reverse("categories-api:index")
        response = self.client.get(
            url, {"search": "Category", "country_id": self.country1.id}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["country"], self.country1.id)
        self.assertEqual(response.data[0]["title"], self.category1.title)
        self.assertEqual(response.data[1]["title"], self.category2.title)

    def test_category_list_api_view_with_country_filter_only(self):
        url = reverse("categories-api:index")
        response = self.client.get(url, {"country_id": self.country2.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["country"], self.country2.id)
        self.assertEqual(response.data[0]["title"], self.category3.title)
        self.assertEqual(response.data[1]["title"], self.category4.title)
