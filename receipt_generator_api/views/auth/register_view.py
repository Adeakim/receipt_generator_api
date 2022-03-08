from django.contrib.auth import authenticate

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import status
from django.shortcuts import get_object_or_404
from receipt_generator_api import serializers


# from rest_framework.response import Response

from receipt_generator_api.lib.response import Response
from receipt_generator_api import models
from receipt_generator_api.serializers import user_serializer
# from serializers.user_serializer import RegisterSerializer


class AuthenticationViewset(ViewSet):

    queryset = models.User.objects.all()
    

    @action(detail=False, methods=["post"], url_path="register", url_name="register")
    def register(self, request):
        serializer = user_serializer.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)