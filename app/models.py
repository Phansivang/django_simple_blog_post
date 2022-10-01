from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
now = timezone.now()
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title
