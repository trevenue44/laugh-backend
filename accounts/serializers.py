from rest_framework import serializers
from .models import Laugher


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = Laugher
        fields = ("username", "password")

    def create(self, validated_data):
        return Laugher.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laugher
        fields = ["username"]
