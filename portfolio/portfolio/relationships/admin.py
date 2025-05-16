from django.contrib import admin
from .models import School, Student

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','address']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','roll','school']
