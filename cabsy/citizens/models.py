from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Citizen(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='Edad', blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    avatar = models.URLField(max_length=400, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.is_staff = False
        super(Citizen, self).save(*args, **kwargs)
