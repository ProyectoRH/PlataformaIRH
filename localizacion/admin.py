from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin
from .models import Localizacion

from documentos_digitales.models import DocumentoDigital
from documentos_shape.models import DocumentoShape


class DocumentoDigitalInline(admin.StackedInline):
    model = DocumentoDigital
    extra = 1

    exclude = ('institucion', )

    def save_model(self, request, obj, form, change):
		perfil = UserProfile.objects.get(usuario = request.user)
		obj.institucion = perfil.institucion
		obj.save()


class DocumentoShapeInline(admin.StackedInline):
    model = DocumentoShape
    extra = 1


class LocalizacionAdmin(LeafletGeoAdmin):
    model = Localizacion
    inlines = [DocumentoDigitalInline, DocumentoShapeInline]



class MiLocalizacion(Localizacion):
    class Meta:
        proxy = True


admin.site.register(MiLocalizacion, LocalizacionAdmin)
