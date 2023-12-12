from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate_email(self, email):
        # Check if there is username with this email
        if not User.objects.filter(username=email).exists():
            raise ValidationError("There is no user with this email")

        return email

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        # Check if login information is correct
        user = authenticate(username=email, password=password)
        if not user:
            raise ValidationError("Invalid email or password")

        data["user"] = user
        return data


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate_email(self, email):
        # Check if there is username with this email
        if User.objects.filter(username=email).exists():
            raise ValidationError(f"{email} is already taken.")

        return email

    def validate_password(self, password):
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters.")

        return password
