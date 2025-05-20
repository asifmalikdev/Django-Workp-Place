# views.py

from django.views import View
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

class StudentView(View):
    def get(self, request):
        form = StudentForm()
        students = Student.objects.all()
        return render(request, 'student_combined.html', {
            'form': form,
            'students': students
        })

    def post(self, request):
        form = StudentForm(request.POST)
        students = Student.objects.all()
        if form.is_valid():
            form.save()
            return redirect('student_combined')
        return render(request, 'student_combined.html', {
            'form': form,
            'students': students
        })
