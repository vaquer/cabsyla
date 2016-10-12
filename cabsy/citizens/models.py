from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Citizen(AbstractUser):
    country = models.CharField(default='Mexico', max_length=50)
    city = models.CharField(max_length=3, choices=settings.STATES_MEXICO, default='9')
    age = models.PositiveIntegerField(verbose_name='Edad', blank=True, null=True)


    class Meta:
        verbose_name = 'Citizen'
