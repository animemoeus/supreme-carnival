from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

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

        user = authenticate(
            self.request,
            username=form.cleaned_data.get("email"),
            password=form.cleaned_data.get("password"),
        )
        if user:
            login(request, user)
            return redirect("accounts:home")

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


class HomeView(TemplateView):
    def get(self, request):
        return render(request, "accounts/home.html")
