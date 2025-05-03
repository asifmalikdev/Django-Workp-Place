from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    def post(self, request, *args, **kwargs):
        return render(request, 'dashboard.html')

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

class CustomPasswordResetView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'password_reset.html')

# class PasswordResetConfirmView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'password_reset_confirm.html')
