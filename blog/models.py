from django.db import models
from django.utils import timezone
from users.models import User


class Post(models.Model):
    """A single blog post"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateField(auto_now_add=True)
    published_date = models.DateField(blank=True, null=True, default=timezone.now)
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title
