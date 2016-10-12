from __future__ import unicode_literals
from django.db import models
from model_utils.models import TimeStampedModel
from drivers.models import Driver


# Create your models here.
class Complaint(TimeStampedModel):
    trip = models.CharField(max_length=70, db_index=True)
    driver = models.ForeignKey(Driver, verbose_name='driver', related_name='complaints')
    subject = models.CharField(max_length=150, choices=settings.COMPLAINTS_SUBJECT)
    comment = models.TextField()


class Compliment(TimeStampedModel):
    trip = models.CharField(max_length=70, db_index=True)
    driver = models.ForeignKey(Driver, verbose_name='driver', related_name='compliments')
    subject = models.CharField(max_length=150, choices=settings.COMPLIMENTS_SUBJECT)
    comment = models.TextField()