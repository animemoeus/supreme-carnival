from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=25, unique=True)
    flag = models.URLField(max_length=255)
    currency = models.CharField(max_length=5, unique=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return self.name
