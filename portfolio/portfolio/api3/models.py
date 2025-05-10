from django.db import models

class Api3Students(models.Model):
    name = models.CharField(max_length=30)
    fname = models.CharField(max_length=20)
    city = models.CharField(max_length=30)

