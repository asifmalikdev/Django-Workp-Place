from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    city = models.CharField(max_length=20)
# Create your models here.
class StudentDumy(models.Model):
    nam=models.CharField(max_length=30)
    fnam=models.CharField(max_length=30)