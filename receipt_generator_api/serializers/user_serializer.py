import re

from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

# from models import User
from receipt_generator_api import models

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = models.User
        fields = ("id", "name", "email", "mobile_number", "password", "confirm_password")
        extra_kwargs = {
            "password": {"write_only": True},
            "confirm_password": {"write_only": True},
        }
        Write_only_fields = ["password", "confirm_password"]

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if confirm_password != password:
            raise ValidationError("Passwords mismatch")
        return data

    def save(self):
        user = models.User(
            name=self.validated_data["name"], email=self.validated_data["email"], mobile_number=self.validated_data["mobile_number"]
        )
        user.set_password(self.validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("email", "password")
