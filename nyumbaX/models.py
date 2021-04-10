from django.db import models
from django.utils import timezone
from users.models import User
# Create your models here.


class Business(models.Model):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
