from django.db import models
from django.utils import timezone


class Topic(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey("users.User", related_name="topics", on_delete=models.SET_NULL, null=True)

    is_deleted = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Topic: {self.title}"


class Entry(models.Model):
    content = models.TextField()
    topic = models.ForeignKey("topics.Topic", related_name="entries", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name="entries", on_delete=models.SET_NULL, null=True)

    is_deleted = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Entry: {self.id}"


class Vote(models.Model):
    entry = models.ForeignKey("topics.Entry", related_name="votes", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name="votes", on_delete=models.SET_NULL, null=True)

    is_liked = models.BooleanField()

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        is_liked_text = "liked" if self.is_liked else "disliked"
        return f"Vote: Entry {self.entry_id} is {is_liked_text} by {self.user.username}"
