from django.urls import path

from .views import CheckDestinationView

urlpatterns = [
    path("", CheckDestinationView.as_view(), name="index"),
]

app_name = "destination"
