from django.contrib import admin
from .models import CabGroup, Driver


# Register your models here.
@admin.register(CabGroup)
class CabGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'created',)
    exclude = ('ranking', 'slug',)
    list_filter = ('name', 'country', 'city', 'enabled',)

    class Meta:
        model = CabGroup


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('completeName', 'country', 'city', 'created',)
    exclude = ('ranking', 'slug',)
    list_filter = ('name', 'country', 'city', 'enabled', 'birthday',)

    class Meta:
        model = Driver
