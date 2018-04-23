from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Debate(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=280, null=False)
    body = models.TextField(blank=True)
    image = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header


class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.creator.username)
