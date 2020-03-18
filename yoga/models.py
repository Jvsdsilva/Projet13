from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404


class UploadImage(models.Model):
    title = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.jpg")

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=3000)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(blank=True)

    def __str__(self):
        return self.title
