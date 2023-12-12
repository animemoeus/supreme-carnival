from django.urls import path

from .views import CountryView, CreateCountryView, DeleteCountryView, EditCountryView

urlpatterns = [
    path("", CountryView.as_view(), name="index"),
    path("create/", CreateCountryView.as_view(), name="create"),
    path("<int:pk>/edit/", EditCountryView.as_view(), name="edit"),
    path("<int:pk>/delete/", DeleteCountryView.as_view(), name="delete"),
]

app_name = "countries"
