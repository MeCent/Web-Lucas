from django.urls import path
from . import views

urlpatterns = [
    path('<str:routine_slug>', views.routine_details, name = 'routine_details'),
]
