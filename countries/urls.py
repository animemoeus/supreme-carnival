from django.urls import path

from .views import AddCountryView, CountryView, DeleteCountryView, EditCountryView

urlpatterns = [
    path("", CountryView.as_view(), name="index"),
    path("add/", AddCountryView.as_view(), name="add"),
    path("<int:pk>/edit/", EditCountryView.as_view(), name="edit"),
    path("<int:pk>/delete/", DeleteCountryView.as_view(), name="delete"),
]

app_name = "countries"
