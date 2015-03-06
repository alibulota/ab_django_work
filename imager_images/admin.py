from django.contrib import admin
from models import Photo, Album
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Photo)
admin.site.register(Album)
