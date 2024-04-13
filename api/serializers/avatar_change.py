from rest_framework import serializers

class AvatarChangeSerializer(serializers.Serializer):
    avatar = serializers.ImageField(required=True)
