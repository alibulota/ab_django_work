from django.db import models
from django.contrib.auth.models import User


class ImagerProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_image', blank=True)
    birthday = models.DateField('date of birth', null=True)
    phone = models.PhoneNumberField('phone number', unique=True, db_index=True)
    

    def __unicode__(self):
        return self.user.username


class Variable(models.Model):
    is_active = models.BooleanField(default=True)

