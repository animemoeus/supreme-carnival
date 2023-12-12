from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .api.serializers import LoginSerializer
from .forms import LoginForm, RegisterForm


class LoginView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("accounts:home"))

        return render(request, "accounts/login.html", context={"form": LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        context = {"form": form}

        if not form.is_valid():
            return render(request, "accounts/login.html", context)

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect(reverse("accounts:home"))
        else:
            context["errors"] = ["Invalid username or password"]

        return render(request, "accounts/login.html", context)


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("accounts:home"))

        return render(
            request, "accounts/register.html", context={"form": RegisterForm()}
        )

    def post(self, request):
        form = RegisterForm(request.POST)
        context = {"form": form}

        if not form.is_valid():
            return render(request, "accounts/register.html", context)

        user = form.save()

        if user:
            return redirect(reverse("accounts:registration-success"))

        return render(request, "accounts/register.html", context)


def index(request):
    # return HttpResponse("Hello World!")
    return render(request, "accounts/base.html")


class HomeView(TemplateView):
    def get(self, request):
        user = request.user

        if not user.is_authenticated:
            return redirect("accounts:login")

        return render(request, "accounts/home.html")
