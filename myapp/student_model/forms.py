from django import forms
from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):
    
    class Meta:
        model=Student
        fields='__all__'
        widgets = {
            'gender': forms.RadioSelect,
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
    