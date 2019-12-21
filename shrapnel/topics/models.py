from django.db import models
from django.utils import timezone


class Topic(models.Model):
    title = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey("users.User", related_name="topics", on_delete=models.SET_NULL, null=True)

    is_deleted = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"
        ordering = ['date_created']

    def __str__(self):
        return f"Topic: {self.title}"


class Entry(models.Model):
    content = models.TextField()
    topic = models.ForeignKey("topics.Topic", related_name="entries", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name="entries", on_delete=models.SET_NULL, null=True)

    is_deleted = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        ordering = ['date_created']

    def __str__(self):
        return f"Entry: {self.id}"


class Vote(models.Model):
    entry = models.ForeignKey("topics.Entry", related_name="votes", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name="votes", on_delete=models.SET_NULL, null=True)

    is_liked = models.BooleanField()

    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        is_liked_text = "liked" if self.is_liked else "disliked"
        return f"Vote: Entry {self.entry_id} is {is_liked_text} by {self.user.username}"
