from django.urls import path

from .views import AddCountryView, CountryView, EditCountryView

urlpatterns = [
    path("", CountryView.as_view(), name="index"),
    path("add/", AddCountryView.as_view(), name="add"),
    path("<int:pk>/edit/", EditCountryView.as_view(), name="edit"),
]

app_name = "countries"
