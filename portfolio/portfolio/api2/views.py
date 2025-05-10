import json

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Student
from .serializers import StudentsSerializers
from rest_framework import serializers
from .models import Students
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from .forms import StudentsForm

def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_api_view')


    else:
        form = StudentsForm()
    return render(request, 'add_student.html', {'form': form})


@api_view(['GET'])
def student_api_view(request):
    stu = Students.objects.all()

    serializer = StudentsSerializers(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    json_data = json.dumps(serializer.data)
    return render(request, 'student_view.html', {"json_data": json_data})

def api_JsonResponse(request):
    stu = Students.objects.all()
    serializer = StudentsSerializers(stu, many=True)
    return JsonResponse(serializer.data, safe=False)

