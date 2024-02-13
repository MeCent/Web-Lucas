from django.shortcuts import render
from .models import Service, Carousel

def servicios(request):
    service = Service.objects.all()
    carousel = Carousel.objects.all()
    data = {
        'service': service,
        'carousel': carousel,
    }
    return render(request, 'pages/servicios.html', data)