from django.db import models

class Routines(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    objetivo = models.TextField(max_length=500)
    observaciones = models.TextField(max_length=500)
    is_active = models.BooleanField(default=False)
    slug_routine = models.SlugField(max_length=200, unique='True')
