from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import Student
from .form import studentForm
# Create your views here.

#@login_required(login_url='/login/')
def index(request):
    student_list = Student.objects.order_by('student_lastname')
    template = loader.get_template('profil.html')
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'student_list': student_list,
    }
    return HttpResponse(template.render(context, request))

def select(request):
    student_list = Student.objects.order_by('student_lastname')
    template = loader.get_template('select.html')
    context = {
        'student_list': student_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, student_id):
    student_info = Student.objects.get(pk=student_id)
    template = loader.get_template('../template/detail.html')
    context = {
        'student_info': student_info
    }
    return HttpResponse(template.render(context, request))

