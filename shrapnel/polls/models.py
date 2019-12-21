from django.db import models
from django.utils import timezone


class Poll(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey("users.User", related_name="polls", on_delete=models.SET_NULL, null=True)

    date_created = models.DateTimeField(default=timezone.now)
    date_expiration = models.DateTimeField()

    def __str__(self):
        return f"Poll: {self.title}"


class PollOption(models.Model):
    body = models.CharField(max_length=100)
    poll = models.ForeignKey("polls.Poll", related_name="options", on_delete=models.CASCADE)

    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"PollOption: \"{self.body}\", Poll: \"{self.poll.title}\""


class PollAnswer(models.Model):
    user = models.ForeignKey("users.User", related_name="poll_answers", on_delete=models.SET_NULL, null=True)
    poll = models.ForeignKey("polls.Poll", related_name="answers", on_delete=models.CASCADE)
    option = models.ForeignKey("polls.PollOption", on_delete=models.CASCADE)

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "poll")

    def __str__(self):
        return f"PollAnswer: by {self.user.username}, Poll: \"{self.poll.title}\""
