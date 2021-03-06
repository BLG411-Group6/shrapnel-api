from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import LoginSerializer, UserSerializer


class RegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class LoginView(GenericAPIView):
    queryset = User.objects.filter(is_deleted=False)
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            raise AuthenticationFailed

        data = dict()
        token, created = Token.objects.get_or_create(user=user)
        data["token"] = token.key

        return Response(data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class HelloView(APIView):
    """
    This view will be used to get CSRF token.
    """

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)
