from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm
from .models import *

# Create your views here.
def student(request):
    if (request.method=='POST'):
        form=StudentForm(request.POST)
        if(form.is_valid):
            form.save()
            return HttpResponse("Student Registered Successfully")
    else:
        form=StudentForm()

    return render(request,"student_model/register.html",{'form': form})
