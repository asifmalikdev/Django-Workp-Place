from functools import partial

from django.contrib.staticfiles.views import serve
from django.core.serializers import serialize
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin,
                                   CreateModelMixin, UpdateModelMixin, DestroyModelMixin)
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentModelViewSetJWT(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer= StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data saved in d.b'})
        return Response(serializer.errors)
    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu,data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":" complete updated"})
        return Response(serializer.errors)
    def partial_update(self,request, pk):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"partial upate complete"})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'msg':"data delted"})










class StudentListMixin(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StudentCreateMixin(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentRetrieveMixin(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class StudentUpdateView(UpdateModelMixin, GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class StudentDeleteMixin(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)























from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class StudentCRUDView(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




























class StudentAPI(APIView):
    def get(self, request, pk=None , format=None):
        id = pk
        print('id : ', id)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=404)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)

    def post(self, request, format = None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg', 'data created'})
        return Response(serializer.errors)

    def put(self, request, pk=None, format = None):
        id = pk
        print(id)
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'})
        return Response(serializer.errors)

    def patch(self, request, p=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data patched succecfully'})
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'deleted'})

@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        print('id : ', id)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=404)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)


    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg', 'data created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = pk
        print(id)
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'msg':'deleted'})

    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data patched succecfully'})
        return Response(serializer.errors)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def studentsapi(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            try:
                stu=Student.objects.get(pk=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({"error":"student not found"})
        else:
            stu = Student.objcets.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Student saved'})
        else:
            return Response(serializer.errors)
    elif request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"student updated"})
        else:
            return Response(serializer.errors)
    elif request.method == "PATCH":
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "student saved"})
        return Response(serializer.errors)
    elif request.method == "DELETE":
        try:
            id = pk
            stu = Student.objects.get(id = pk)
            stu.delete()
            return Response({"msg":"Student Deleted"})
        except Student.DoesNotExist:
            return Response({"msg":"studen does not exist"})