from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('profil/', include('profil.urls')),
    path('politique/', views.politique),
    path('logout/', views.logout)
]
