from api.urls import urlpatterns
from . import views
from django.urls import path

urlpatterns=[
    path('api3/', views.student_details, name="api3")

]