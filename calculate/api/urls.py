from django.urls import path

from .views import CalculateAPIView

urlpatterns = [
    path("", CalculateAPIView.as_view(), name="index"),
]

app_name = "calculate"
