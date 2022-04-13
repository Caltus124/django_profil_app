from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('register/', views.register),
    path('profil/', include('profil.urls')),
    path('home/', views.home),
    path('logout/', views.logout)
]

