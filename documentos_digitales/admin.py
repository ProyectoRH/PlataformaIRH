from django.contrib import admin
from documentos_digitales.models import DocumentoDigital
from .models import Idioma, Nivel

admin.site.register(Idioma)
admin.site.register(Nivel)
# Register your models here.

class DocDigitalAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		print "guardando documento"
		obj.usuario = request.user
		institucion = request.user.institucion
		nucleo = Nucleo.objects.get(institucion = institucion)

		obj.nucleo = nucleo
		obj.save()

admin.site.register(DocumentoDigital, DocDigitalAdmin)
