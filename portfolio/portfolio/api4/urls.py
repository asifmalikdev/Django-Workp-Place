from django.urls import path
from . import views
from .views import (StudentAPI, StudentListMixin, StudentCreateMixin,
                    StudentUpdateView, StudentRetrieveMixin, StudentDeleteMixin, StudentCRUDView)

urlpatterns = [

    path('student_api/', views.student_api, name='student_api'),
    path('student_api/<int:pk>', views.student_api, name='student_api'),
    path('StudentAPI/',StudentAPI.as_view(), name="StudentAPI"),
    path('StudentAPI/<int:pk>', StudentAPI.as_view(), name="StudentAPI"),
    path('StudentListMixin/',StudentListMixin.as_view(), name = "StudentListMixin" ),
    path('StudentListMixin/<int:pk>', StudentRetrieveMixin.as_view(), name="StudentRetrieveMixin"),
    path('StudentCreateMixin/', StudentCreateMixin.as_view(), name="StudentCreateMixin"),
    path('StudentUpdateView/<int:pk>', StudentUpdateView.as_view(), name="StudentUpdateView"),
    path('StudentDeleteMixin/<int:pk>', StudentDeleteMixin.as_view(), name="StudentDeleteMixin" ),
    path('StudentCRUDView/', StudentCRUDView.as_view(), name="StudentCRUDView"),
    path('StudentCRUDView/<int:pk>', StudentCRUDView.as_view(), name="StudentCRUDView"),

]
