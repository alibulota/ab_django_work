from dimager.models import ImagerProfile
from dimager.models import Photo, Albums
from django.contrib.auth.models import User
from django.test import TestCase
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    username = 'elenore'


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

        image = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )


class TestCase_ImagerProfile(TestCase):
    def setUp(self):
        self.test_user = UserFactory.create()

    def test_create_profile(self):
        '''Test that every user gets a profile'''
        assert self.test_user.profile

    def test_delete_profile(self):
        '''Test that profile deleted from database'''
        self.test_user.delete()
        assert len(ImagerProfile.objects.all()) == 0

    def test_is_active(self):
        '''Test that user is active user'''
        assert self.test_user.profile.is_active()


class TestCase_FollowBlock(TestCase):
    def setUp(self):
        self.elenore = UserFactory()
        self.rigby = UserFactory(username='rigby')

    def test_followers(self):
        '''Test for follower relationship'''
        self.elenore.profile.follow(self.rigby.profile)
        self.assertIn(self.elenore.profile, self.rigby.profile.followers())

    def test_following_list(self):
        '''Test for following relationship'''
        self.elenore.profile.follow(self.rigby.profile)
        self.assertIn(self.rigby.profile, self.elenore.profile.following_list())

    def test_follow(self):
        '''Test for ability to follow'''
        self.elenore.profile.follow(self.rigby.profile)
        self.assertIn(self.rigby.profile, self.elenore.profile.following.all())

    def test_unfollow(self):
        '''Test for ability to unfollow'''
        self.elenore.profile.follow(self.rigby.profile)
        self.elenore.profile.unfollow(self.rigby.profile)
        self.assertNotIn(self.rigby.profile, self.elenore.profile.following_list())

    def test_block(self):
        self.elenore.profile.follow(self.rigby.profile)
        self.rigby.profile.block(self.elenore.profile)
        self.assertIn(self.elenore.profile, self.rigby.profile.blocking.all())

    def test_unblock(self):
        '''Test ability to unblock user profile'''
        self.elenore.profile.follow(self.rigby.profile)
        self.rigby.profile.block(self.elenore.profile)
        self.assertIn(self.elenore.profile, self.rigby.profile.blocking.all())
        self.rigby.profile.unblock(self.elenore.profile)
        self.assertNotIn(self.elenore.profile, self.rigby.profile.blocking.all())


class Test_Photo(TestCase):
    def setUp(self):
        self.elenore = UserFactory()
        self.photo = ImageFactory.create(title='test photo', description='test class photo')

    def test_title(self):
        '''Assert that picture contains a title'''
        assert photo.title == 'test photo'

    def test_description(self):
        '''Assert picture contains description'''
        assert photo.description == 'test class photo'

    def test_date_uploaded(self):
        '''Assert photo has upload date or null'''
        assert photo.date_uploaded == now()

    def test_date_modified(self):
        '''Assert photo has modified date or null'''
        assert photo.date_modified == now()

    def test_date_published(self):
        '''Assert photo has published date or null'''
        assert photo.date_published == today()

    def test_private(self):
        '''Assert default privacy option is private; no one can view'''
        assert photo.date_published == True

    def test_shared(self):
        '''Assert option for shared; friends can view'''

    def test_public(self):
        '''Assert option for public; anyone can view that follows'''


class Test_Album(TestCase):
    def setUp(self):
        self.album = AlbumFactory.create(title=test_album, description='test class album')

    def test_user_album(self):
        '''Assert album contains only user's photos'''

    def test_title(self):
        '''Assert that album contains a title'''

    def test_description(self):
        '''Assert album contains description'''

    def test_date_uploaded(self):
        '''Assert album has upload date or null'''

    def test_date_modified(self):
        '''Assert album has modified date or null'''

    def test_date_published(self):
        '''Assert photo has published date or null'''

    def test_private(self):
        '''Assert default privacy option is private; no one can view'''

    def test_shared(self):
        '''Assert option for shared; friends can view'''

    def test_public(self):
        '''Assert option for public; anyone can view that follows'''

    def test_cover(self):
        '''Assert one contained photo as cover for album'''
