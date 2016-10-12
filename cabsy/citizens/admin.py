from django.contrib import admin
from .models import Citizen


# Register your models here.
@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
	list_display = ('username', 'first_name', 'last_name', 'is_active',)
	list_filter = ('username', 'first_name', 'last_name', 'is_active',)
	exclude = ('slug',)
	class Meta:
		model = Citizen