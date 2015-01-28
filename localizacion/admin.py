from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin
from .models import Localizacion

from documentos_digitales.models import DocumentoDigital
from documentos_shape.models import DocumentoShape




class DocumentoDigitalInline(admin.StackedInline):
	model = DocumentoDigital
	extra = 3

class DocumentoShapeInline(admin.StackedInline):
	model = DocumentoShape
	extra = 3

class LocalizacionAdmin(admin.ModelAdmin):
	inlines = [DocumentoDigitalInline, DocumentoShapeInline]


class MiLocalizacion(Localizacion):
	class Meta:
		proxy = True



admin.site.register(Localizacion, LeafletGeoAdmin)
admin.site.register(MiLocalizacion, LocalizacionAdmin)