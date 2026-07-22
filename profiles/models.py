from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    bio = models.TextField(blank=True)

    location = models.CharField(
        max_length=100,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"