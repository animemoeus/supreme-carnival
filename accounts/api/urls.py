from django.urls import path

from . import views
from .views import LoginAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
]

app_name = "accounts"
