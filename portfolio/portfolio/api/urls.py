from django.urls import path
from . import views

urlpatterns=[
    path('studentinfo/<int:id>', views.studentwise_details),
    path('studentinfo/', views.student_details, name="studentinfo"),
    path("student_dummy_form/", views.student_dummy_form, name="student_dummy_form"),
    path("student_show/", views.student_dummy_show, name="student_show"),
    path("student_thirdparty_showing/", views.student_api, name="student_thirdparty_showing"),
    path('student_create/', views.student_create, name ="student_create")
]