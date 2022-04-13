from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('', views.login),
    path('login/', views.login),
<<<<<<< HEAD
    path('register/', views.register),
    path('profil/', include('profil.urls')),
=======
    path('home/', views.home),
    path('register/', views.register)
>>>>>>> 723ed3f0605fa4114e409671c8a8c964c0b6cee6
]

#handler404 = "views.404.html"
