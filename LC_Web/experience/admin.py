from django.contrib import admin
from .models import Experience

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')

admin.site.register(Experience, ExperienceAdmin)