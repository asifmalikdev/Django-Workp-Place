from django.db import models

class StudentCrud(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=30)

# Create your models here.
