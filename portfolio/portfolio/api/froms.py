from django import forms
from .models import StudentDumy
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentDumy
        fields=['nam', 'fnam']
