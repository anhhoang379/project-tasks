from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import LoginSerializer


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access_token": str(refresh.access_token),
                    "user_id": user.id,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
