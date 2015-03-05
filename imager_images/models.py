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

    PRIVATE = 'private'
    SHARED = 'shared'
    PUBLIC = 'public'
    PHOTO_PRIVACY_OPTIONS = (
        (PRIVATE, 'private', ),
        (SHARED, 'shared', ),
        (PUBLIC, 'public', ),
    )

    PUBLISHED = models.CharField(
        max_length=3,
        choices=PHOTO_PRIVACY_OPTIONS,
        default=PRIVATE
    )


class Album(models.Model):
    user = models.ForeignKey(User, related_name='album')
    pictures = models.ManyToManyField(
        Photo,
        related_name='album',
        limit_choices_to={user: 'self'}
    )
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    date_modified = models.DateField(auto_now=True, null=True, blank=True)
    date_publishd = models.DateField(null=True, blank=True)

    PRIVATE = 'private'
    SHARED = 'shared'
    PUBLIC = 'public'
    PHOTO_PRIVACY_OPTIONS = (
        (PRIVATE, 'private', ),
        (SHARED, 'shared', ),
        (PUBLIC, 'public', ),
    )

    PUBLISHED = models.CharField(
        max_length=3,
        choices=PHOTO_PRIVACY_OPTIONS,
        default=PRIVATE
    )
    cover = models.ForeignKey(Photo)
