from django.contrib import admin

# Register your models here.
from .models import Evento
from django.conf import settings
from nucleo.models import Nucleo

class EventoAdmin(admin.ModelAdmin):

	exclude = ('usuario', 'nucleo',)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		institucion = request.user.institucion
		try:
			nucleo = Nucleo.objects.get(institucion = institucion)

			obj.nucleo = nucleo
			obj.save()
		except:
			pass


admin.site.register(Evento, EventoAdmin)