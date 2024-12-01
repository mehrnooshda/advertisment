from django.contrib.auth.models import User
from django.db import models

from user.models import AdUser


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user_id = models.ForeignKey(AdUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    user_id = models.ForeignKey(AdUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
