from django.contrib import admin
from dimager.models import ImagerProfile


class profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_active')


admin.site.register(ImagerProfile)
