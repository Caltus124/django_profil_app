from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student
# Create your views here.

def index(render):
    template = loader.get_template('profil.html')
    return HttpResponse(template.render())

def select(request):
    student_list = Student.objects.order_by('student_lastname')
    template = loader.get_template('../template/select.html')
    context = {
        'student_list': student_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, student_id):
    this_student = Student.objects.get(pk=student_id)
    template = loader.get_template('../template/detail.html')
    context = {
        'firstname': this_student.student_firstname,
        'lastname': this_student.student_lastname,
    }
    return HttpResponse(template.render(context, request))

