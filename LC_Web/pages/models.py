from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField
from ckeditor.fields import RichTextField
import os
from django.core.exceptions import ValidationError
from django.forms import EmailField

# PERFIL

def validate_file_extension_cv(value):
    accepted_extensions = [ '.pdf' ]
    file_extension = os.path.splitext(value.name)[1].lower()
    if file_extension not in accepted_extensions:
        raise ValidationError(f"Formato no Soportado. Solo {', '.join(accepted_extensions)} permitido.")

def validate_file_extension_photo(value):
    accepted_extensions = [ '.jpg', '.jpeg', '.png' ]
    file_extension = os.path.splitext(value.name)[1].lower()
    if file_extension not in accepted_extensions:
        raise ValidationError(f"Formato no Soportado. Solo {', '.join(accepted_extensions)} permitido.")

class OwnerManager(models.Manager):
    def get_or_create_singleton(self):
        owner, created = self.get_or_create(pk=1)
        return owner

class Owner(models.Model):
    name = CharField(max_length=100)

    objects = OwnerManager()
    def save(self, *args, **kwargs):
        if Owner.objects.exists() and not self.pk:
            raise ValidationError("Solo UN ADMIN es permitido.")
        super(Owner, self).save(*args, **kwargs)

    freelance = CharField(max_length=250)
    city = CharField(max_length=100)
    descript = RichTextField(blank=True)
    instagram_link = URLField(max_length=100, blank=True)
    mail = EmailField()
    telephone = URLField(max_length=100, blank=True)
    main_photo = ImageField(upload_to='photos/', validators=[validate_file_extension_photo])
    logo_photo = ImageField(upload_to='photos/', validators=[validate_file_extension_photo])
    cv = models.FileField(upload_to='cv/', validators=[validate_file_extension_cv])

def __str__(self):
    return self.name