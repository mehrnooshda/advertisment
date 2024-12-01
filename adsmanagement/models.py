from django.contrib.auth.models import User
from django.db import models


class Ads(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
