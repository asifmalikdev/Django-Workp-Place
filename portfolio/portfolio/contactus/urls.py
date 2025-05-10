from django.urls import path
from contactus import views  # ✅ CORRECT

urlpatterns=[
    path('contact/', views.contact_view, name='contact'),
    path('thank_you/', views.thankyou_view, name='thank_you' ),
]