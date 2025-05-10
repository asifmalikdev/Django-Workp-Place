from django.shortcuts import render
from .models import Api3Students
from .serializers import Api3Serializer
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def student_details(request):
    stu = Api3Students.objects.all()
    serializer = Api3Serializer(stu, many=True)
    # print(type(JsonResponse(serializer.data)))
    return JsonResponse(serializer.data, safe=False)