from django.shortcuts import render
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework.viewsets import ModelViewSet

class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer