from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register("SchoolViewSet", views.SchoolViewSet, basename="SchoolViewSet"),
router.register("StudentViewSet", views.StudentViewSet, basename="StudentViewSet"),
urlpatterns=[
    path('', include(router.urls)),
]

