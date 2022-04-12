from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home),
    path('login/', views.login),
    path('register/', views.register)
]

#handler404 = "views.404.html"
