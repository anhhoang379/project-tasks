from django.contrib.auth.models import User
from rest_framework import serializers


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ["username", "password", "confirm_password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        confirm_password = validated_data.pop("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match"}
            )

        user = User.objects.create_user(**validated_data, password=password)
        return user
