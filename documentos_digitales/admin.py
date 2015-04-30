from django.contrib import admin
from documentos_digitales.models import DocumentoDigital
from .models import Idioma, Nivel

admin.site.register(Idioma)
admin.site.register(Nivel)
# Register your models here.
