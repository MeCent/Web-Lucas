from django.shortcuts import render
from .models import Service

def servicios(request):
    service = Service.objects.all()
    data = {
        'service': service,
    }
    return render(request, 'pages/servicios.html', data)