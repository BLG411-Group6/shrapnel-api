from random import randint

from rest_framework.test import APIClient

from ..models import User


def create_test_user(data=None):
    if data is None:
        data = dict()

    username = f'test-user-{randint(1, 10000000)}'
    first_name = 'Test'
    last_name = 'User'
    password = 'password'

    data.setdefault('username', username)
    data.setdefault('first_name', first_name)
    data.setdefault('last_name', last_name)
    data.setdefault('email', f'test-user+{username}@shrapnel.com')
    data.setdefault('password', password)

    return User.objects.create_user(**data)


def create_test_user_and_client():
    user = create_test_user()
    client = APIClient()
    client.force_login(user)

    return user, client
