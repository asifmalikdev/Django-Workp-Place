from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def landing_page(request):
    users = User.objects.all()
    superuser_names = [x.username for x in users if x.is_superuser]
    print(superuser_names)
    return render(request, 'landing.html', {"user": users} )

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

def index_view(request):
    return render(request, 'index.html')



