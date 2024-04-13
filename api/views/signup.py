from rest_framework import generics, status
from rest_framework.response import Response

from ..serializers import SignUpSerializer


class SignUpView(generics.CreateAPIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
