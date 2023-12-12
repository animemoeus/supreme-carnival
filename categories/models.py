from django.db import models

from countries.models import Country


class Category(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    price_per_kilo = models.FloatField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title
