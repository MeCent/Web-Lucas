from django.shortcuts import render, get_object_or_404
from .models import Owner

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')



def estudios(request):
    return render(request, 'pages/estudios.html')

def experiencia(request):
    return render(request, 'pages/experiencia.html')

def contacto(request):
    return render(request, 'pages/contacto.html')