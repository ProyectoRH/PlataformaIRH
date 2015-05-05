from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin
from .models import Localizacion

from documentos_digitales.models import DocumentoDigital
from documentos_shape.models import DocumentoShape

from nucleo.models import Nucleo
from django.conf import settings


class DocumentoDigitalInline(admin.StackedInline):
    model = DocumentoDigital
    extra = 1



class DocumentoShapeInline(admin.StackedInline):
  model = DocumentoShape
  extra = 1


class LocalizacionAdmin(LeafletGeoAdmin):
    model = Localizacion
    inlines = [DocumentoDigitalInline, DocumentoShapeInline]

    exclude = ('usuario', 'nucleo',)

    def save_model(self, request, obj, form, change):
      obj.usuario = request.user
      institucion = request.user.institucion
      nucleo = Nucleo.objects.get(institucion = institucion)

      obj.nucleo = nucleo
      obj.save()


class MiLocalizacion(Localizacion):
    class Meta:
        proxy = True


admin.site.register(MiLocalizacion, LocalizacionAdmin)
