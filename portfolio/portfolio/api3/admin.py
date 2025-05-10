from calendar import month

from django.contrib import admin
from .models import Api3Students

@admin.register(Api3Students)
class Api3StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'fname', 'city']


# Register your models here.
