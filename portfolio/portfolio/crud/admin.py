from django.contrib import admin
from .models import StudentCrud

@admin.register(StudentCrud)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'roll', 'city']


# Register your models here.
