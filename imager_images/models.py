from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    picture = models.ImageField(upload_to='photos')
    user = models.ForeignKey(User, related_name='photo')
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date_uploaded = models.DateField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateField(auto_now=True, null=True, blank=True)
    date_publishd = models.DateField(null=True, blank=True)


class Album(models.Model)
