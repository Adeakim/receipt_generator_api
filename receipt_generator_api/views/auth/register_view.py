from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework import status, mixins, viewsets

from receipt_generator_api.lib.response import Response
from receipt_generator_api import models
from receipt_generator_api.serializers import user_serializer


class AuthenticationViewset(viewsets.GenericViewSet):

    queryset = models.User.objects.all()
    serializer_class = user_serializer.RegisterSerializer

    @action(detail=False, methods=["post"], url_path="register", url_name="register")
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)