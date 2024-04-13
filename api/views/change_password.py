from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import ChangePasswordSerializer


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")

            if not check_password(old_password, request.user.password):
                return Response(
                    "The old password is incorrect.",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            request.user.password = make_password(new_password)
            request.user.save()
            return Response(
                "Password was successfully changed.", status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
