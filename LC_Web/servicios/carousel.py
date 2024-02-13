from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_file_extension_photo(value):
    accepted_extensions = [ '.jpg', '.jpeg', '.png' ]
    file_extension = os.path.splitext(value.name)[1].lower()
    if file_extension not in accepted_extensions:
        raise ValidationError(f"Formato no Soportado. Solo {', '.join(accepted_extensions)} permitido.")

class Carousel(models.Model):
    image = models.ImageField(upload_to='photos/examples/', validators=[validate_file_extension_photo])
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=250)

    def __str__(self):
        return self.title