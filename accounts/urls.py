from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import HomeView, LoginView, RegisterView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "register/success/",
        TemplateView.as_view(template_name="accounts/registration-success.html"),
        name="registration-success",
    ),
]

app_name = "accounts"
