from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin
from .models import Localizacion

from documentos_digitales.models import DocumentoDigital
from documentos_shape.models import DocumentoShape




class DocumentoDigitalInline(admin.TabularInline):
	model = DocumentoDigital
	extra = 3

class DocumentoShapeInline(admin.TabularInline):
	model = DocumentoShape
	extra = 3

class LocalizacionAdmin(admin.ModelAdmin):
	inlines = [DocumentoDigitalInline, DocumentoShapeInline]




admin.site.register(Localizacion, LeafletGeoAdmin)
# LocalizacionAdmin