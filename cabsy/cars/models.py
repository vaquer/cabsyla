from __future__ import unicode_literals
import hashlib
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel


# Create your models here.
class Car(TimeStampedModel):
    modelcar = models.CharField(max_length=300)
    yearcar = models.PositiveIntegerField(blank=False)
    tags = models.CharField(max_length=15, blank=False)
    startservicedate = models.DateTimeField()
    qrstringcode = models.CharField(max_length=100, blank=False, db_index=True)

    def __unicode__(self):
        return u'{0} {1}'.format(self.modelcar, self.yearcar)

    def generate_qr_string(self):
        string_raw_qr = '{0}{1}{2}'.format(self.modelcar.encode('utf-8'), str(self.yearcar), self.tags)
        return hashlib.sha224(string_raw_qr)

    def save(self):
        if not self.id:
            self.qrstringcode = self.generate_qr_string()
        super(Car, self).save()

