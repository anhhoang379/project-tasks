from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import AvatarChangeSerializer


class AvatarChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AvatarChangeSerializer(data=request.data)
        if serializer.is_valid():
            avatar = serializer.validated_data["avatar"]

            request.user.avatar = avatar
            request.user.save()
            return Response(
                "Avatar đã được thay đổi thành công.",
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
