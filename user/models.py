from django.contrib.auth.models import AbstractUser
from django.db import models

class AdUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email