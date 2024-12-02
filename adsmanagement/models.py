from django.db import models

from advertisement import settings
from user.models import AdUser


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ads')
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
