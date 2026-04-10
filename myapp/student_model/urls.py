from django.urls import path
from . import views

urlpatterns = [
    path('',views.student,name='student'),
    path('student_list/',views.student_list,name='student_list')
    
]