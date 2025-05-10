"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from portfolio import views
from django.http import JsonResponse

urlpatterns = [

    path('index/', views.index_view, name='index'),
    path('', views.landing_page, name = "landing"),
    path('home/', views.home, name = 'home'),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contact/', include("contactus.urls")),
    path('api/',include("api.urls")),
    path('api2/',include("api2.urls")),
    path('api3/', include("api3.urls")),
    path('crud/', include("crud.urls")),
    path('api4/', include("api4.urls")),
]

