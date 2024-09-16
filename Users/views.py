# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('portfolio_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
