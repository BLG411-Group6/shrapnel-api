from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ..models import User
from .utils import create_test_user, create_test_user_and_client


class RegistrationViewTests(TestCase):
    def setUp(self):
        self.url = reverse('users:register')
        self.client = APIClient()

    def test_successful_registration(self):
        payload = {
            'email': 'testuser@shrapnel.com',
            'username': 'testusername',
            'first_name': 'A',
            'last_name': 'B',
            'password': 'password',
            'repeated_password': 'password'
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(id=response.data['id'])
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
        self.assertIsNone(response.data.get('password'))

    def test_registration_with_invalid_email(self):
        payload = {
            'email': 'invalid',
            'username': 'testusername',
            'first_name': 'A',
            'last_name': 'B',
            'password': 'password',
            'repeated_password': 'password',
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'Enter a valid email address.')

    def test_registration_with_mismatching_password(self):
        payload = {
            'email': 'testuser@shrapnel.com',
            'username': 'testusername',
            'first_name': 'A',
            'last_name': 'B',
            'password': 'password',
            'repeated_password': 'differentpassword'
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], 'Passwords you have entered do not match!')

    def test_registration_with_taken_username(self):
        user = create_test_user({'username': 'testuser'})
        payload = {
            'email': 'testuser@shrapnel.com',
            'username': user.username,
            'first_name': 'A',
            'last_name': 'B',
            'password': 'password',
            'repeated_password': 'password'
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['username'][0], 'user with this username already exists.')


class LoginViewTests(TestCase):
    def setUp(self):
        self.url = reverse('users:login')

        self.username = 'testuser'
        self.password = 'helloworld'

        self.user = create_test_user({'username': self.username, 'password': self.password})
        self.client = APIClient()

    def test_successful_login(self):
        payload = {'username': self.username, 'password': self.password}
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unsuccessful_login(self):
        payload = {'username': self.username, 'password': 'wrongpassword'}
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LogoutViewTests(TestCase):
    def setUp(self):
        self.url = reverse('users:logout')
        self.user, self.client = create_test_user_and_client()

    def test_logout(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
