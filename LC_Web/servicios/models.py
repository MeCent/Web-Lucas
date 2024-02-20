from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
import os

def validate_file_extension_photo(value):
    accepted_extensions = [ '.jpg', '.jpeg', '.png' ]
    file_extension = os.path.splitext(value.name)[1].lower()
    if file_extension not in accepted_extensions:
        raise ValidationError(f"Formato no Soportado. Solo {', '.join(accepted_extensions)} permitido.")

class Service(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    description = models.TextField()
    benefits = RichTextField(blank=True)

    def __str__(self):
        return self.title

class Carousel(models.Model):
    image = models.ImageField(upload_to='photos/examples/', validators=[validate_file_extension_photo])
    imgtitle = models.CharField(max_length=150)
    imgsubtitle = models.CharField(max_length=250)

    def __str__(self):
        return self.imgtitle
