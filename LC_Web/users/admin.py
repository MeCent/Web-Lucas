from django.contrib import admin
from .models import Profile
"""
from django.utils.html import format_html

class OwnerAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="25" style="border-radius:50px" />'.format(object.image))
    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'name')

"""

admin.site.register(Profile)
