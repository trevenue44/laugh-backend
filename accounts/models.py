from django.db import models
from django.contrib.auth.models import AbstractUser


class Laugher(AbstractUser):
    REQUIRED_FIELDS = []

    # using the username as the display name on the admin site.
    def __str__(self) -> str:
        return self.username
