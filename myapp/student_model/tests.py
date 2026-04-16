from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Student

class StudentTestCase(TestCase):

    # ✅ Test 1: Student Create
    def test_student(self):
        student = Student.objects.create(
          name="Suba",
          email="suba@gmail.com",
          dob="2000-01-01"
          )
        self.assertEqual(student.name, "Suba")

    # ✅ Test 2: Student List Page Load
    def test_student_list(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)

    

    # ✅ Test 4: Delete Student
    def test_delete_student(self):
        student = Student.objects.create(
            name="Delete Me",
            email="delete@gmail.com",
            dob="2000-01-01"
            )
        response = self.client.get(reverse('delete_student', args=[student.id]))
        self.assertEqual(response.status_code, 302)