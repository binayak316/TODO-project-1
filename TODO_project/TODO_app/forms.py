from django import forms
from django.forms import ModelForm

from .models import *
class myTaskForm(forms.ModelForm):
    class Meta:
        model = myTask
        fields = '__all__'



