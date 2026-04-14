from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import *
from django.contrib import messages
from openpyxl import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


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
    format = request.GET.get('format')

    if format == 'excel':
        wb = Workbook()
        ws = wb.active
        ws.append(["Name", "Student ID", "Mobile", "Email", "Date of Birth", "Gender", "Address"])

        students = Student.objects.all()
        for s in students:
            ws.append([s.name,s.id, s.mobile_no, s.email, s.dob, s.gender, s.address])

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=students.xlsx'
        wb.save(response)
        return response

    elif format == 'pdf':
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="students.pdf"'

        students = Student.objects.all()
        data = [["Name", "Student ID", "Mobile", "Email", "Date of Birth", "Gender", "Address"]]

        for s in students:
            data.append([s.name,s.id, s.mobile_no, s.email, s.dob, s.gender, s.address])

        doc = SimpleDocTemplate(response)
        table = Table(data)
        doc.build([table])

        return response


    students = Student.objects.all()
    return render(request, 'student_model/student_list.html', {'students': students})



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


