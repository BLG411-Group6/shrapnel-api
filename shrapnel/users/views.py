from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

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

        login(request, user)

        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutView(APIView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class HelloView(APIView):
    """
    This view will be used to get CSRF token.
    """

    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)
