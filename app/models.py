from django.db import models

# Create your models here.


class Chat(models.Model):
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    description = models.TextField()
