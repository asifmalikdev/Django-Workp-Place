from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer

class StudentApiView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(pass_by = user)

from django_filters.rest_framework import DjangoFilterBackend
class DjangoFilterStudent(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']


from rest_framework.filters import SearchFilter
class DjangoSearchStudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','city']


from rest_framework.filters import OrderingFilter
class DjangoOrderingStudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']

from rest_framework.generics import ListAPIView
from .mypaginations import MyPageNumberPagination
class PaginationDjangoStudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination



