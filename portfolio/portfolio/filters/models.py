from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.PositiveIntegerField()
    pass_by = models.CharField(max_length=100)