import re

from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from models import User

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=200, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ("id", "name", "email", "phone_number", "password", "confirm_password")
        extra_kwargs = {
            "password": {"write_only": True},
            "confirm_password": {"write_only": True},
        }
        Write_only_fields = ["password", "confirm_password"]

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if confirm_password != password:
            raise ValidationError("The two passwords must be the same")
        return data
    
    def validate_phone_number(self, phone_number):
        regex = re.compile(r"^\+?[0-9]+$")
        if regex.match(phone_number):
            return phone_number
        raise serializers.ValidationError("Enter a valid phone number")


    def save(self):
        user = User(
            name=self.validated_data["name"], email=self.validated_data["email"], phone_number=self.validated_data["phone_number"]
        )
        user.set_password(self.validated_data["password"])
        user.save()
        return user
