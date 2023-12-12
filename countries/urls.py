from django.urls import path

from .views import CountryView

urlpatterns = [
    path("", CountryView.as_view(), name="index"),
]

app_name = "countries"
