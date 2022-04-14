from django.forms import ModelForm
from django import forms

from .models import *

class studentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'