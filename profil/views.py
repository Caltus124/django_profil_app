from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(render):
    return HttpResponse("Ici Futur CRUD")

def select(render):
    return HttpResponse("Ici futur selection")

def detail(render):
    return HttpResponse("Ici futur detail")
