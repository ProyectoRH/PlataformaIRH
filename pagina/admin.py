from django.contrib import admin
from .models import Pagina
from django.conf import settings
from nucleo.models import Nucleo
#from django.contrib.auth.models import User

class PaginaAdmin(admin.ModelAdmin):
	
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

admin.site.register(Pagina, PaginaAdmin)