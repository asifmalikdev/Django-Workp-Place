from django.contrib import admin
from django.urls import path, include
from .views import HomeView, LoginView, RegistrationView, CustomPasswordResetView
urlpatterns = [
    path('', HomeView.as_view(), name = 'home' ),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegistrationView.as_view(), name = 'register'),
    path('password_reset/', CustomPasswordResetView.as_view(), name = 'password_reset')

]

