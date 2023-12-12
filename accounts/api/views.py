from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer, RegisterSerializer


class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate access and refresh token
        refresh = RefreshToken.for_user(serializer.validated_data.get("user"))
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        User.objects.create_user(
            username=serializer.validated_data.get("email"),
            email=serializer.validated_data.get("email"),
            password=serializer.validated_data.get("password"),
        )
        return Response(
            {"message": "User created successfully."}, status=status.HTTP_201_CREATED
        )
