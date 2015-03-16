from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dimager.models import ImagerProfile
from imager_images.models import Album, Photo, User
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView


@login_required()
def user_profile(request, id):
    user = User.objects.get(id=id)
    try:
        albums = Album.objects.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    num_photos = Photo.objects.filter(user=user).count()
    return render(request, 'profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'num_photo': num_photos
    })


@login_required()
def user_profile(request):
    user = request.user
    try:
        albums = Album.objects.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    num_photos = Photo.objects.filter(user=user).count()
    return render(request, 'profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'num_photo': num_photos
    })


@login_required()
def library(request):
    user = request.user_profile
    try:
        albums = Album.objects.filter(user=user).all()
    except:
        albums = None
    try:
        photos = Photo.objects.filter(user=user).all()
    except:
        photos = None
    return render(request, 'library.html', {
        'user': user,
        'albums': albums,
        'photos': photos
    })


class ImagerProfileUpdateView(UpdateView):
    model = ImagerProfile
    template_name_suffix = '_update_form'
    success_url = '/profile/'
    fields = [
        'profile_image',
        'phone_number',
        'birthday',
        'phone_privacy',
        'birthday_privacy',
        'picture_privacy',
        'name_privacy',
        'email_privacy',
        'following',
        'blocking',
    ]

    def get_queryset(self):
        qs = super(ImagerProfileUpdateView, self).get_queryset()
        return qs.filter(user=self.request.user)
