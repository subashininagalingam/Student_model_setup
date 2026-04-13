from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import *
from django.contrib import messages

# Create your views here.
def student(request):
    if (request.method=='POST'):
        form=StudentForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('success')
    else:
        form=StudentForm()

    return render(request,"student_model/register.html",{'form': form})

def success(request):
    return render(request,"student_model/success.html")

def student_list(request):
    students=Student.objects.all()
    return render(request,"student_model/student_list.html",{'students':students})

def edit_student(request, id):
    student=Student.objects.get(id=id)
    if (request.method=='POST'):
        student.name=request.POST.get('name')
        student.mobile_no=request.POST.get('mobile_no')
        student.email=request.POST.get('email') 
        student.dob=request.POST.get('dob')
        student.address=request.POST.get('address')
        student.save()
        return redirect('student_list')
    return render(request, "student_model/edit_student.html", {'student': student})

        

def delete_student(request, id):
    student=Student.objects.get(id=id)
    student.delete()
    messages.success(request, "✅Student deleted successfully")
    return redirect('student_list')


