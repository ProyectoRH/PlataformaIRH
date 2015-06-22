from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin
from .models import Localizacion

from documentos_digitales.models import DocumentoDigital
from documentos_shape.models import DocumentoShape

from nucleo.models import Nucleo
from Mediciones.models import Medicion
from django.conf import settings


class DocumentoDigitalInline(admin.StackedInline):
    model = DocumentoDigital
    extra = 1

class DocumentoShapeInline(admin.StackedInline):
    model = DocumentoShape
    extra = 1

class MedicionesInline(admin.StackedInline):
    model = Medicion
    extra = 1

class LocalizacionAdmin(LeafletGeoAdmin):
    model = Localizacion
    inlines = [DocumentoDigitalInline, DocumentoShapeInline, MedicionesInline]

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

    @property
    def media(self):
        media = super(LocalizacionAdmin, self).media
        js = ["js/test.js",]
        media.add_js(js)
        return media

class MiLocalizacion(Localizacion):
    class Meta:
        proxy = True


admin.site.register(MiLocalizacion, LocalizacionAdmin)
