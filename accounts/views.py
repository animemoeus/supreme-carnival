from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import LoginForm


class LoginView(TemplateView):
    def get(self, request):
        # If user is authenticated, redirect to home page
        if request.user.is_authenticated:
            return redirect(reverse("accounts:home"))

        return render(request, "accounts/login.html", context={"form": LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        context = {"form": form}

        if not form.is_valid():
            return render(request, "accounts/login.html", {"errors": form.errors})

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect(reverse("accounts:home"))
        else:
            context["errors"] = ["Invalid username or password"]

        return render(request, "accounts/login.html", context)


def index(request):
    # return HttpResponse("Hello World!")
    return render(request, "accounts/base.html")


def home(request):
    return render(request, "accounts/home.html")
