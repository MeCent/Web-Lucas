from django.contrib import admin
from .models import Service, Carousel

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'benefits', 'image')

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'subtitle')

admin.site.register(Service, ServiceAdmin)

admin.site.register(Carousel, CarouselAdmin)