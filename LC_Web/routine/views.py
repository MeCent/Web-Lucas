from django.shortcuts import render

def routine_details(request):
    return render(request, 'pages/routine_details.html')