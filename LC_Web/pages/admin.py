from django.contrib import admin
from .models import Owner
from django.utils.html import format_html

class OwnerAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="25" style="border-radius:50px" />'.format(object.main_photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'name')

admin.site.register(Owner, OwnerAdmin)