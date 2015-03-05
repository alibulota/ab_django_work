from django.test import TestCase
from django.contrib.auth.models import User
from dimager.models import ImagerProfile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'Butters'


class TestCase_ImagerProfile(TestCase):
    def setUp(self):
        self.test_user = UserFactory.create()

    def test_create_profile(self):
        '''Test that every user gets a profile'''
        assert self.test_user.ImagerProfile

    def test_delete_profile(self):
        '''Test that profile deleted from database'''
        self.test_user.delete()
        assert len(ImagerProfile.objects.all()) == 0

    def test_is_active(self):
        '''Test that user is active user'''
        assert self.test_user.ImagerProfile.is_active()
