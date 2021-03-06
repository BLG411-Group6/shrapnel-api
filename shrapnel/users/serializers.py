from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token

from .models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    repeated_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'repeated_password',
            'first_name',
            'last_name',
        )

    def validate(self, data):
        data = super().validate(data)

        password = data.get('password')
        repeated_password = data.pop('repeated_password', None)

        if password and (password != repeated_password):
            raise ValidationError({'password': 'Passwords you have entered do not match!'})

        return data

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(user.password)
        user.save()
        Token.objects.create(user=user)
        return user
