from django.db import models
from django.utils import timezone


class DirectMessage(models.Model):
    title = models.CharField(max_length=50)
    # TODO: Hash content.
    content = models.TextField()
    sender = models.ForeignKey("users.User", related_name="direct_messages_sent", on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey("users.User", related_name="direct_messages_received", on_delete=models.SET_NULL, null=True)

    is_read = models.BooleanField(default=False)

    is_deleted_by_sender = models.BooleanField(default=False)
    is_deleted_by_receiver = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "DirectMessage"
        verbose_name_plural = "DirectMessages"

    def __str__(self):
        return f"Direct Message: from {self.sender.username} to {self.receiver.username}"
