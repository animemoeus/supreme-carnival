from django.urls import path

from .views import AddCountryView, CountryView

urlpatterns = [
    path("", CountryView.as_view(), name="index"),
    path("add/", AddCountryView.as_view(), name="add"),
]

app_name = "countries"
