import os
from django.db import models
from django.forms import ValidationError


def validate_file_extension_photo(value):
    accepted_extensions = [ '.jpg', '.jpeg', '.png' ]
    file_extension = os.path.splitext(value.name)[1].lower()
    if file_extension not in accepted_extensions:
        raise ValidationError(f"Formato no Soportado. Solo {', '.join(accepted_extensions)} permitido.")

class Routines(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    objetivo = models.TextField(max_length=500)
    observaciones = models.TextField(max_length=500)
    is_active = models.BooleanField(default=False)
    slug_routine = models.SlugField(max_length=200, unique='True')
    routine_cover = models.ImageField(upload_to='routine/', validators=[validate_file_extension_photo])
    video_link = models.URLField(max_length=100, blank=True)
