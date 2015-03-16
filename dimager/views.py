from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dimager.models import ImagerProfile
from imager_images.models import Album, Photo
from django.contrib.auth.decorators import login_required


@login_required
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
