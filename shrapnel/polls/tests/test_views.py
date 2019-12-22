from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from shrapnel import settings
from ..models import Poll, PollOption
from shrapnel.users.tests.utils import create_test_user_and_client


class PollsViewTests(TestCase):
    def setUp(self):
        self.url = reverse('polls:polls')
        self.user, self.client = create_test_user_and_client()
        self.datetime_format = settings.REST_FRAMEWORK['DATETIME_FORMAT']

    def test_create_poll(self):
        payload = {
            "title": "Test Poll",
            "options": [
                {"body": "Option A"},
                {"body": "Option B"}
            ],
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        poll = Poll.objects.get(id=response.data["id"])
        self.assertEqual(response.data["title"], poll.title)
        self.assertEqual(response.data["date_expiration"], poll.date_expiration.strftime(self.datetime_format))
        self.assertEqual(response.data["date_created"], poll.date_created.strftime(self.datetime_format))
        self.assertEqual(response.data["options"][0]["body"], payload["options"][0]["body"])
        self.assertEqual(response.data["options"][1]["body"], payload["options"][1]["body"])

    def test_list_polls(self):
        poll = Poll.objects.create(
            title="Test Poll",
            user=self.user,
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], poll.id)
        self.assertEqual(response.data[0]["title"], poll.title)
        self.assertEqual(response.data[0]["user"]["id"], poll.user.id)
        self.assertEqual(response.data[0]["user"]["username"], poll.user.username)


class PollDetailsViewTests(TestCase):
    def setUp(self):
        self.user, self.client = create_test_user_and_client()

        self.datetime_format = settings.REST_FRAMEWORK['DATETIME_FORMAT']

        self.poll = Poll.objects.create(
            title="Test Poll",
            user=self.user,
        )
        self.poll_option = PollOption.objects.create(
            body="Option A",
            poll=self.poll
        )
        self.url = reverse('polls:poll-detail', args=[self.poll.id])

    def test_poll_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.poll.id)
        self.assertEqual(response.data["title"], self.poll.title)
        self.assertEqual(response.data["user"]["username"], self.poll.user.username)
        self.assertEqual(response.data["date_expiration"], self.poll.date_expiration.strftime(self.datetime_format))
        self.assertEqual(response.data["date_created"], self.poll.date_created.strftime(self.datetime_format))
        self.assertEqual(response.data["options"][0]["id"], self.poll_option.id)
        self.assertEqual(response.data["options"][0]["body"], self.poll_option.body)

    def test_poll_update(self):
        payload = {"title": "Update Poll Title"}
        response = self.client.patch(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.poll.id)
        self.assertEqual(response.data["title"], payload["title"])

    def test_delete_poll(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PollOptionsViewTests(TestCase):
    def setUp(self):
        self.user, self.client = create_test_user_and_client()

        self.datetime_format = settings.REST_FRAMEWORK['DATETIME_FORMAT']

        self.poll = Poll.objects.create(
            title="Test Poll",
            user=self.user,
        )
        self.url = reverse('polls:poll-options', args=[self.poll.id])

    def test_list_poll_options(self):
        poll_option = PollOption.objects.create(
            body="Option A",
            poll=self.poll
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], poll_option.id)
        self.assertEqual(response.data[0]["body"], poll_option.body)

    def test_create_poll_option(self):
        payload = {"body": "Option A"}
        response = self.client.post(self.url, data=payload)
        poll_option = PollOption.objects.get(id=response.data["id"])
        self.assertEqual(response.data["body"], poll_option.body)
        self.assertEqual(response.data["date_created"], poll_option.date_created.strftime(self.datetime_format))
        self.assertEqual(response.data["number_of_answers"], 0)


class PollAnswerViewTests(TestCase):
    def setUp(self):
        self.user, self.client = create_test_user_and_client()

        self.datetime_format = settings.REST_FRAMEWORK['DATETIME_FORMAT']

        self.poll = Poll.objects.create(
            title="Test Poll",
            user=self.user,
        )
        self.poll_option_1 = PollOption.objects.create(
            body="Option 1",
            poll=self.poll
        )
        self.poll_option_2 = PollOption.objects.create(
            body="Option 2",
            poll=self.poll
        )

        self.url = reverse('polls:poll-answers', args=[self.poll.id, self.poll_option_1.id])

    def test_poll_answer(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["option"]["id"], self.poll_option_1.id)
        self.assertEqual(response.data["option"]["body"], self.poll_option_1.body)
        self.assertEqual(response.data["poll"]["options"][0]["number_of_answers"], 1)
        self.assertEqual(response.data["poll"]["options"][1]["number_of_answers"], 0)

        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0], "You have already voted.")
