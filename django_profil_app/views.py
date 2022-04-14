from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
import os
import socket

def login(request):
    hname = os.uname()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            user = form.get_user()
            request.session[0] = username
            if username == 'admin':
                print(socket.gethostbyname(socket.gethostname()) + " Connexion de l'admin ! avec : " + str(hname))
                return redirect('../profil?user=' + username, user=username)
            elif username != 'admin':
                print("Connexion de " + username + " avec : " + str(hname))
                return redirect('../profil/select?user=' + username)
            else:
                return redirect('/login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def politique(request):
    return render(request, 'politique.html')


