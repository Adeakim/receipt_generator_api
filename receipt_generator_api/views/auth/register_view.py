from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
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

class UserViewset(viewsets.GenericViewSet):
    queryset= models.User.objects.all()
    serializer_class = user_serializer.RegisterSerializer
    permission_class = [IsAuthenticated]

    def list(self, request, *arg, **kwargs):
        """
        Returns a list of plans for the currently
        authenticated user that owns the plans.
        """
        # plans = Plan.objects.all()
        users = models.User.objects.all()
        serializer = self.get_serializer(users, many=True)
        # self.check_object_permissions(users)
        return Response(
            data=dict(users=serializer.data, total=len(serializer.data)),
            status=status.HTTP_200_OK,
        )
