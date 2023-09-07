from django.shortcuts import render
from .models import Experience

def experience(request):
    experience = Experience.objects.all()
    data = {
        'experience': experience,
    }
    return render(request, 'pages/experiencia.html', data)