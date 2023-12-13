from rest_framework import filters
from rest_framework.generics import ListAPIView

from countries.models import Country
from countries.serializer import CountrySerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all().order_by("-id")
    serializer_class = CountrySerializer

    filter_backends = [filters.SearchFilter]
    search_fields = [
        "name",
    ]
