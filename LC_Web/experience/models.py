from django.db import models
from ckeditor.fields import RichTextField

class Experience(models.Model):

    type_of_that_thing = (
        ('Education', 'Education'),
        ('Experience', 'Experience'),
    )

    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    description = RichTextField()
    category = models.CharField(max_length=100, choices=type_of_that_thing)

    def __str__(self):
        return self.title