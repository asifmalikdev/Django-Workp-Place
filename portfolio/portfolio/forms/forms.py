from .models import Assignment, Question
from django.forms.models import inlineformset_factory
from django import forms
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"