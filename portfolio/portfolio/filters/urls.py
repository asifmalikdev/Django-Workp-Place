from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("StudentView", views.StudentApiView, basename="StudentView"),
router.register("DjangoFilterStudent", views.DjangoFilterStudent, basename="DjangoFilterStudent"),

urlpatterns=[
    path('DjangoSearchStudent/', views.DjangoSearchStudent.as_view(), name="DjangoSearchStudent"),
    path('DjangoOrderingStudent/', views.DjangoOrderingStudent.as_view(), name="DjangoOrderingStudent"),
    path("PaginationDjangoStudent/", views.PaginationDjangoStudent.as_view(), name="PaginationDjangoStudent"),
    path('', include(router.urls)),
]