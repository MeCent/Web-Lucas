from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            form.save()
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'pages/registro.html', {'form': form})