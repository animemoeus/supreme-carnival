from rest_framework.response import Response
from rest_framework.views import APIView

from calculate.serializers import CaculateAPISerializer
from calculate.utils import get_domestic_price, get_international_price
from categories.models import Category
from countries.models import Country


class CalculateAPIView(APIView):
    def post(self, request):
        serializer = CaculateAPISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        origin = (
            Country.objects.filter(id=serializer.validated_data.get("country_id"))
            .first()
            .name
        )
        destination = serializer.validated_data.get("destination_id")
        category = Category.objects.filter(
            id=serializer.validated_data.get("category_id")
        ).first()
        international_price = get_international_price(
            serializer.validated_data.get("weight"), category.price_per_kilo
        )
        domestic_price = get_domestic_price(
            serializer.validated_data.get("weight"), category.price_per_kilo
        )
        total_price = international_price + domestic_price

        response = {
            "origin": origin,
            "destination": f"{destination.get('province')}, {destination.get('city_name')}, {destination.get('postal_code')}",
            "category_name": category.title,
            "international_price": international_price,
            "domestic_price": domestic_price,
            "total_price": total_price,
        }
        return Response(response)
