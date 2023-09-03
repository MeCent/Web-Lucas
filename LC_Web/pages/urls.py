from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('estudios/', views.estudios, name='estudios'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('contacto/', views.contacto, name='contacto'),
]