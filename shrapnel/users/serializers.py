from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


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
        raw_password = validated_data.pop('password')
        user = super(UserSerializer, self).create(validated_data)

        user.set_password(raw_password)
        user.save(update_fields=['password'])

        return user
