from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'benefits', 'example_photos')

admin.site.register(Service, ServiceAdmin)