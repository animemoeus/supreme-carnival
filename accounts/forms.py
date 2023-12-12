from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not User.objects.filter(username=email).exists():
            raise forms.ValidationError(f"There is no user with this email.")

        return email

    def clean(self):
        cleaned_data = super().clean()

        user = authenticate(
            username=cleaned_data.get("email"),
            password=cleaned_data.get("password"),
        )
        if not user and cleaned_data.get("password"):
            self.add_error("password", "Invalid password.")

        return cleaned_data


class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(username=email).exists():
            raise forms.ValidationError(f"{email} is already used by another user.")

        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters.")

        return password

    def save(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = User.objects.create_user(username=email, email=email, password=password)

        return user
