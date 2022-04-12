from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def error(request, exception):
    return render(request, '404.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('/login')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'register.html', {'form': form})