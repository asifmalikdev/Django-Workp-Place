from django.contrib import admin
from .models import Assignment, Question
from .forms import QuestionForm, AssignmentForm

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    min_num =1
    can_delete=True

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = [field.name for field in Assignment._meta.fields]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]