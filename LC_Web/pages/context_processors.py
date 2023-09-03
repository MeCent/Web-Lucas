from .models import Owner
from django.shortcuts import get_object_or_404

def information(request):
    return {
        'owner': get_object_or_404(Owner, pk=1)
    }
