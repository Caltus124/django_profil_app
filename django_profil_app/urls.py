from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('profil/', include('profil.urls')),
    path('politique/', views.politique),
    path('logout/', views.logout)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
