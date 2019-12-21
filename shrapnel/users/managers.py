from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        user = self.model(
            username=username,
            is_staff=is_staff,
            is_superuser=is_superuser,
            date_created=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username=None, password=None, **extra_fields):
        return self._create_user(username, password, is_staff=False, is_superuser=False, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, is_staff=True, is_superuser=True, **extra_fields)
