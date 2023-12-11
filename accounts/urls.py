from django.urls import path

from . import views
from .views import LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("home/", views.home, name="home"),
]

app_name = "accounts"
