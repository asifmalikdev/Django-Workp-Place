from api.urls import urlpatterns
from . import views
from django.urls import path

urlpatterns=[
    path('add/', views.add_student, name='add'),
    path('student_api_view/', views.student_api_view, name='student_api_view'),
    path('api_JsonResponse/', views.api_JsonResponse, name="api_JsonResponse"),

]
