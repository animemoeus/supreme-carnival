from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password")


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
