import io

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

from crud.serializers import StudentSerializer

@csrf_exempt
def student_create_in_db(request):
    # print("asif")
    if request.method == "POST":
        json_data = request.body
        # print("here i have the json data",json_data)
        stream = io.BytesIO(json_data)
        # print("here i have the stream data", stream)
        python_data = JSONParser().parse(stream)
        # print("python_data data is here", python_data)
        serializer = StudentSerializer(data = python_data)
        # print("serializer data is here", serializer)
        if serializer.is_valid():
            serializer.save()
            # print(serializer,"serizerhdfjhdfhskdjhf ajsdh jadhfj")
            res = {
                "msg": "data inserted in db"
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")

from .models import StudentCrud
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
def deletingentry(request):
    try:
        temp = StudentCrud.objects.get(id=1)
        temp.delete()
        return JsonResponse({"message": "student deleted"})
    except:
        return JsonResponse({"error":"student does not exist"})