from django.urls import path

from . import views

app_name = 'profil'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>/', views.detail, name='detail'),
    path('profil', views.index, name='profil'),
    path('select', views.select, name='select')

]






