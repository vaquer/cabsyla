from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify
from django.conf import settings
from model_utils.models import TimeStampedModel
#from cities.models import Country, City
from cars.models import Car


# Create your models here.
class CabGroup(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False)
    adress = models.CharField(max_length=700, blank=False)
    country = models.CharField(default='Mexico', max_length=50)
    city = models.CharField(max_length=3, choices=settings.STATES_MEXICO)
    president = models.CharField(max_length=300, blank=False)
    ranking = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    enabled = models.BooleanField(default=False)
    slug = models.SlugField(max_length=150, db_index=True)

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.name, self.country, self.city)

    def save(self):
        if not self.id:
            pre_slug = '{0} {1} {2}'.format(self.name, self.country, self.city)
            slug = slugify(pre_slug)
            count = CabGroup.objects.filter(slug__startswith=slug).count()

            if count > 0:
                self.slug = '{0}-{1}'.format(slug, str(count))

            self.slug = slug
        super(CabGroup, self).save()


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
    ranking = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    enabled = models.BooleanField(default=False)
    estatus = models.CharField(max_length=1, choices=settings.DRIVER_STATUS, default='P')
    cabgroupdriver = models.ForeignKey(CabGroup, related_name='drivers', blank=True, null=True)
    slug = models.SlugField(max_length=150, db_index=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.completeName, self.city)

    @property
    def completeName(self):
        return u'{0} {1}'.format(self.name, self.last_name)

    def save(self):
        if not self.id:
            pre_slug = '{0} {1}'.format(self.completeName, self.birthday.strftime('%Y %m %d'))
            slug = slugify(pre_slug)
            self.slug = slug

        super(Driver, self).save()