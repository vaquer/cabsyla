from django.contrib import admin
from .models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('modelcar', 'tags', 'yearcar',)
    exclude = ('qrstringcode', 'qrcode',)
    list_filter = ('modelcar', 'tags', 'yearcar',)

    class Meta:
        model = Car
