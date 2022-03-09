from django.contrib.auth import authenticate

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import status,permissions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken


# from rest_framework.response import Response

from receipt_generator_api.lib.response import Response
from receipt_generator_api.models import User
from receipt_generator_api.serializers import user_serializer
# from serializers.user_serializer import RegisterSerial

class LoginViewset(ViewSet):
    queryset = User.objects.all()        
    serializer_class = user_serializer.LoginSerializer
    permission_class = (permissions.AllowAny,)

    @action(detail=False, methods=["post"], url_path="login", url_name="login")
    def login(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        if email is None or password is None:
            return Response(errors={"error":"Enter valid email and password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if not user:
             return Response(errors={"error":"Ensure both email and password are correct"}, status=status.HTTP_400_BAD_REQUEST)

        # token = RefreshToken.for_user(user).access_token
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={"token":str(token.key), "id":user.id}, status=status.HTTP_200_OK)
