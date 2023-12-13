from django.urls import path

from .views import CountryListAPIView

urlpatterns = [
    path("", CountryListAPIView.as_view(), name="index"),
]

app_name = "countries"
