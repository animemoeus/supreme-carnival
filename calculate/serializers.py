from rest_framework import serializers
from rest_framework.serializers import Serializer

from app.utils import RajaOngkir
from categories.models import Category
from countries.models import Country


class CaculateAPISerializer(Serializer):
    country_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    destination_id = serializers.IntegerField()
    weight = serializers.IntegerField()

    def validate_country_id(self, value):
        """
        Check from Country models from Countries app
        """

        if not Country.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid `country_id`.")

        return value

    def validate_category_id(self, value):
        """
        Check from Category models from Categories app
        """

        if not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid `category_id`.")

        return value

    def validate_destination_id(self, value):
        """
        Use RajaOngkir to validate destination_id
        """

        raja_ongkir = RajaOngkir()
        if not raja_ongkir.validate_city_id(value):
            raise serializers.ValidationError("Invalid `destination_id`.")

        return raja_ongkir.validate_city_id(value)

    def validate_weight(self, value):
        if value <= 0:
            raise serializers.ValidationError("Weight should be a positive integer.")

        return value
