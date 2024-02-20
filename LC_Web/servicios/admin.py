from django.contrib import admin
from .models import Service, Carousel

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description', 'benefits')

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('image', 'imgtitle', 'imgsubtitle')

admin.site.register(Service, ServiceAdmin)

admin.site.register(Carousel, CarouselAdmin)