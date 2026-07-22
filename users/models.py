from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_job_seeker = models.BooleanField(default=True)
    is_business_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.username