from __future__ import unicode_literals
import hashlib
import qrcode
from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class Car(TimeStampedModel):
    modelcar = models.CharField(max_length=300)
    yearcar = models.PositiveIntegerField(blank=False)
    tags = models.CharField(max_length=15, blank=False)
    startservicedate = models.DateTimeField()
    qrStringCode = models.CharField(max_length=100, blank=False, db_index=True)
    qrCode = models.ImageField(upload_to='qrCodes')

    def generate_qr_string(self):
        string_raw_qr = '{0}{1}{2}'.format(self.modelcar.encode('utf-8'), str(self.yearcar), self.tags)
        return hashlib.sha224(string_raw_qr)

    def save(self, *args, **kwargs):
        if not self.id:
            self.qrStringCode = self.generate_qr_string()
            self.qrcode = qrcode.make(self.qrStringCode)
        super(Car, self).save(*args, **kwargs)

