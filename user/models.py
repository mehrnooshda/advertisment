from django.contrib.auth.models import AbstractUser
from django.db import models

class AdUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    def __str__(self):
        return self.email