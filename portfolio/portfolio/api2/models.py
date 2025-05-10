from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=30)
    clas = models.IntegerField()
    roll = models.IntegerField()
    city = models.CharField(max_length=30, null= True)
# Create your models here.
