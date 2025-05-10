from . import views
from django.urls import path

urlpatterns=[
    path("stuCreateExternal/", views.student_create_in_db, name = "stuCreateEternal"),
    path('deletingentry/', views.deletingentry, name="deletingentry"),
]