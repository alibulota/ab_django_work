from django.contrib import admin
from imager_images.models import Album, Photo
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class ImagerProfileInline(admin.StackedInline):
    model = Album, Photo
    can_delete = False
    verbose_name_plural = 'imager albums'


class UserAdmin(UserAdmin):
    inlines = (ImagerProfileInline, )

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
# from dimager.models import ImagerProfile
# from dimager.models import UserAdmin
# from dimager.models import profileAdmin


# class ImagerProfileInline(admin.StackedInline):
#     model = ImagerProfile
#     can_delete = False
#     verbose_name_plural = 'ImagerProfile'


# class UserAdmin(UserAdmin):
#     inlines = (ImagerProfileInline, )


# class profileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'is_active')


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(ImagerProfile, profileAdmin)


admin.site.register(Album)
admin.site.register(Photo)
