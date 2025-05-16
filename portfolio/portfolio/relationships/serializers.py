from rest_framework import serializers
from .models import School, Student



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','roll','school']

class SchoolSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(many=True, read_only=True)
    all_student_info = StudentSerializer(many=True, read_only=True, source="student")
    class Meta:
        model = School
        fields = ['id', 'name','address','student', 'all_student_info']
