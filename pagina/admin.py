from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Pagina
from django.conf import settings
from nucleo.models import Nucleo
#from django.contrib.auth.models import User

class PaginaAdmin(admin.ModelAdmin):
	
	exclude = ('usuario', 'nucleo',)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		institucion = request.user.institucion
		nucleo = Nucleo.objects.get(institucion = institucion)

		obj.nucleo = nucleo
		obj.save()


admin.site.register(Pagina, PaginaAdmin)