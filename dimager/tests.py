from django.test import TestCase
from django.contrib.auth.models import User
from dimager.models import ImagerProfile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'elenore'


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


class TestCase_FollowBlock(TestCase):
    def setUp(self):
        self.elenore = UserFactory()
        self.rigby = UserFactory(username='rigby')

    def test_followers(self):
        '''Test for follower relationship'''
        self.elenore.ImagerProfile.follow(self.rigby.ImagerProfile)
        self.assertIn(self.elenore.ImagerProfile, self.rigby.ImagerProfile.followers.all())

    def test_following(self):
        '''Test for following relationship'''
        self.elenore.ImagerProfile.follow(self.rigby.ImagerProfile)
        self.assertIn(self.elenore.ImagerProfile, self.rigby.ImagerProfile.following.all())

    def test_follow(self):
        '''Test for ability to follow'''
        self.elenore.ImagerProfile.follow(self.rigby.ImagerProfile)
        self.assertIn(self.elenore.ImagerProfile, self.rigby.ImagerProfile.follow.all())

    def test_unfollow(self):
        self.elenore.ImagerProfile.follow(self.rigby.ImagerProfile)
        self.rigby.ImagerProfile.unfollow(self.elenore.ImagerProfile)
        self.assertNotIn(self.rigby.ImagerProfile, self.elenore.ImagerProfile.follow())

    def test_blcok(self):
        self.elenore.ImagerProfile.follow(self.rigby.ImagerProfile)
        self.rigby.ImagerProfile.block(self.elenore.ImagerProfile)
        self.assertNotIn(self.rigby.ImagerProfile, self.elenore.ImagerProfile.following())

    def test_unblock(self):
        '''Test ability to unblock user profile'''
        self.elenore.ImagerProfile.follow(self.rigby.ImagerProfile)
        self.rigby.ImagerProfile.block(self.elenore.ImagerProfile)
        self.assertNotIn(self.rigby.ImagerProfile, self.elenore.ImagerProfile.following())
        self.rigby.ImagerProfile.unblock(self.elenore.ImagerProfile)
        self.assertIn(self.rigby.ImagerProfile, self.elenore.ImagerProfile.following())
