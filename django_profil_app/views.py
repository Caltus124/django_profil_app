from django.http import HttpResponse
from django.shortcuts import render


def error(request, exception):
    return render(request, '404.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')