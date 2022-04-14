from django.urls import path

from . import views

app_name = 'profil'
urlpatterns = [
    path('', views.index, name='index'),
    path('select', views.select, name='selection'),
    path('<int:student_id>/', views.detail, name='detail'),
    path('profil', views.index, name='profil')

]






