import datetime

from django.db import models, IntegrityError
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class Poll(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey("users.User", related_name="polls", on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(default=timezone.now)
    date_expiration = models.DateTimeField()

    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"

    def __str__(self):
        return f"Poll: {self.title}"

    def save(self, *args, **kwargs):
        self.date_expiration = timezone.now() + datetime.timedelta(days=30)
        super().save(*args, **kwargs)


class PollOption(models.Model):
    body = models.CharField(max_length=100)
    poll = models.ForeignKey("polls.Poll", related_name="options", on_delete=models.CASCADE)

    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "PollOption"
        verbose_name_plural = "PollOptions"

    def __str__(self):
        return f"PollOption: \"{self.body}\", Poll: \"{self.poll.title}\""


class PollAnswer(models.Model):
    user = models.ForeignKey("users.User", related_name="poll_answers", on_delete=models.SET_NULL, null=True)
    poll = models.ForeignKey("polls.Poll", related_name="answers", on_delete=models.CASCADE)
    option = models.ForeignKey("polls.PollOption", on_delete=models.CASCADE)

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "PollAnswer"
        verbose_name_plural = "PollAnswers"
        unique_together = ("user", "poll")

    def __str__(self):
        return f"PollAnswer: by {self.user.username}, Poll: \"{self.poll.title}\""

    def save(self, *args, **kwargs):
        self.clean()
        try:
            super().save(*args, **kwargs)
        except IntegrityError:
            raise ValidationError("You have already voted.")
