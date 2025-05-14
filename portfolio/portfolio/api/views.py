import io
import json
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Student as MyAppStudent, StudentDumy
from .froms import StudentForm
from .serializers import StudentSerialziser, StudentDummySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        msg = ""

        python_data = json.loads(request.body)
        name = python_data['name']
        if MyAppStudent.objects.filter(name=name).exists():
            msg = 'this user already exists'
            return JsonResponse({'message': msg}, safe=False)
        serializer = StudentSerialziser(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg = "data is saved in student table"
        else:
            msg = "data is not stored, an error occured"
        print(msg)

        return JsonResponse({'message': msg}, safe=False)






def studentwise_details(request, id):
    stu= MyAppStudent.objects.get(id = id)  #fetching data from Student Model where id = 1, row wise

    serializer = StudentSerialziser(stu) #converted complex data to python data

    json_data = JSONRenderer().render(serializer.data)  #here i have converted python data to json data like in the form api
    return HttpResponse(json_data, content_type='application/json')  #here i have sented data to FE in the form of api

def student_details(request):
    stu = MyAppStudent.objects.all()
    serializer = StudentSerialziser(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data, type(json_data))
    return HttpResponse(json_data, content_type='application/json')

def student_dummy_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentinfo')
    else:
        form = StudentForm()

    return render(request, "stu.html", {"form":form} )
def student_dummy_show(request):
    stu = StudentDumy.objects.all()
    serializer = StudentDummySerializer(stu, many=True)
    json_data = json.dumps(serializer.data)
    print(json_data, type(json_data))

    return render(request, "student_view_dumy.html", {"json_data":json_data})

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            try:
                stu= MyAppStudent.objects.get(id = id)
                serializer = StudentSerialziser(stu)

            except MyAppStudent.DoesNotExists:
                return JsonResponse({'error': 'student does not found'})
        else:
            stu = MyAppStudent.objects.all()
            serializer = StudentSerialziser(stu, many=True)
        print('serializer data is here', serializer.data)
        json_string = JSONRenderer().render(serializer.data)
        print('api data is here', type(json_string), json_string)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        try:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            serializer = StudentSerialziser(data = python_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"msg": "student added in db"}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "PATCH":
        print("asif 1")
        try:
            print("asif 2")
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            if not id:
                print("asif 3")
                return JsonResponse({"error": "id is required for update"}, status=400)
            try:
                print("asif 4")
                stu=MyAppStudent.objects.get(id=id)

            except MyAppStudent.DoesNotExist:
                return JsonResponse({"error ": "student does not exist"}, status= 404)
            serializers = StudentSerialziser(stu, data=python_data, partial=True)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse({"msg": "Student Update Succeccfully"}, status=200)
            return JsonResponse(serializers.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


    elif request.method == 'PUT':
        # print('hello asif in put')
        # temp = request.body
        # print(temp)
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        print("python data is here", python_data)
        if not id:
            return JsonResponse({'error', 'please give an id'})
        stu = MyAppStudent.objects.get(id=id)
        serializer = StudentSerialziser(stu, data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': f'student got update on id " {id}'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

    elif request.method == 'DELETE':
        stream = io.BytesIO(request.body)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        print('id = ', id)
        stu = MyAppStudent.objects.get(id = id)
        stu.delete()
        res = {'msg': 'data deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')


