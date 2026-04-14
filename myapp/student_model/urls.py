from django.urls import path
from . import views

urlpatterns = [
    path('',views.student,name='student'),
    path('success/',views.success,name='success'),
    path('student_list/',views.student_list,name='student_list'),
    path('download_excel/',views.download_excel,name='download_excel'),
    path('download_pdf/',views.download_pdf,name='download_pdf'),
    path('edit_student/<int:id>/',views.edit_student,name='edit_student'),
    path('delete_student/<int:id>/',views.delete_student,name='delete_student'),
    
]