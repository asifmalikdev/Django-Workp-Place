from django.urls import path
from . import views
from .views import StudentAPI

urlpatterns = [

    path('student_api/', views.student_api, name='student_api'),
    path('student_api/<int:pk>', views.student_api, name='student_api'),
    path('StudentAPI/',StudentAPI.as_view(), name="StudentAPI"),
    path('StudentAPI/<int:pk>', StudentAPI.as_view(), name="StudentAPI")

]
