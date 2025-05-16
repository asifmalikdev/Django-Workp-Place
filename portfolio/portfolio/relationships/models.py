from django.db import models
from django.db.models import CASCADE

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(
        School,
        on_delete=CASCADE,
        related_name='student'
    )
    roll = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"
