from django.contrib.auth import authenticate
from rest_framework import status,permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView

from receipt_generator_api.lib.response import Response
from receipt_generator_api.models import User
from receipt_generator_api.serializers import user_serializer

class LoginView(GenericAPIView):
    queryset = User.objects.all()        
    serializer_class = user_serializer.LoginSerializer
    permission_class = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        if email is None or password is None:
            return Response(errors={"error":"Enter valid email and password"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if not user:
             return Response(errors={"error":"Ensure both email and password are correct"}, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken.for_user(user).access_token
        return Response(data={"token":str(token)}, status=status.HTTP_200_OK)
