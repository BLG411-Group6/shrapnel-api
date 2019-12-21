from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .utils import create_test_user, create_test_user_and_client


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
