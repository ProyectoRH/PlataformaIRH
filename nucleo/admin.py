from django.contrib import admin

# Register your models here.
from .models import Nucleo


class NucleoAdmin(admin.ModelAdmin):
	list_display = ('nucleo', 'institucion',)

admin.site.register(Nucleo, NucleoAdmin)
