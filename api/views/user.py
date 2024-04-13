from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from ..serializers import SignUpSerializer


class UserView(generics.CreateAPIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            user_id = request.data.get("user_id")
            user = User.objects.get(id=user_id)
            user.delete()
            return Response(
                "User deleted successfully.", status=status.HTTP_204_NO_CONTENT
            )
        except User.DoesNotExist:
            return Response(
                "User not found.", status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request):
        try:
            user_id = request.data.get("user_id")
            user = User.objects.get(id=user_id)
            serializer = SignUpSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(
                "User not found.", status=status.HTTP_404_NOT_FOUND
            )
