from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
#from cities.models import Country, City
from cars.models import Car


# Create your models here.
class Driver(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    adress = models.CharField(max_length=700, blank=False)
    country = models.CharField(default='Mexico', max_length=50)
    city = models.CharField(max_length=3, choices=settings.STATES_MEXICO)
    licensenumber = models.CharField(max_length=300, blank=False)
    birthday = models.DateTimeField()
    car = models.ForeignKey(Car, null=True, blank=True, related_name='drivers')
    avatar = models.ImageField(upload_to='drivers_avatar')