from django.contrib import admin
from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','roll','pass_by']
    list_filter = ['id', 'pass_by']