from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    city = models.CharField(max_length=20)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance = None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
