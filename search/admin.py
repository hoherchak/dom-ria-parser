from django.contrib import admin

from search.models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Advertisement, AdvertisementAdmin)