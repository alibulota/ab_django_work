from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# from friendship.models import Friend, Follow


class ProfileQuery(models.Model):
    def get_queryset(self):
        qs = super(ProfileQuery, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


class ImagerProfile(models.Model):

    user = models.OneToOneField(User)
    following = models.ManyToManyField(
        'self', related_name='_following', symmetrical=False)
    blocking = models.ManyToManyField(
        'self', related_name='_blocking', symmetrical=False)
    picture = models.ImageField(
        upload_to='profile_image', blank=True, max_length=100)
    picture_privacy = models.BooleanField(default=True)

    birthday = models.DateField('date of birth', null=True)
    birthday_privacy = models.BooleanField(default=True)

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], blank=True, max_length=15)
    phone_privacy = models.BooleanField(default=True)

    name_privacy = models.BooleanField(default=True)
    email_privacy = models.BooleanField(default=True)

    def is_active(self):
        return self.user.is_active

    def __unicode__(self):
        return self.user.username

    def followers(self):
        '''List all users followers'''
        all_followers = Following.objects.sent_requests(user=request.user)
    def following(self):
        '''List of profiles user is following'''
        

    def follow(self):
        '''Create following relationship between profiles'''

    def unfollow(self):
        '''Remove following relationship between profiles'''

