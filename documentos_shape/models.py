# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

from localizacion.models import Localizacion
from nucleo.models import Nucleo


class DocumentoShape(models.Model):
	codigo = models.CharField(max_length=200)
	informacion_sistema_referencia = models.CharField(max_length=200, default='WGS1984')
	nombre = models.CharField(max_length=200)
	version = models.CharField(max_length=200)
	direccion_online = models.URLField(max_length=255)
	archivo = models.FileField(upload_to = "static/documentos_shape")
	localizacion = models.ForeignKey(Localizacion, null=True)
	privado = models.BooleanField(default=False)
	nucleo = models.ForeignKey(Nucleo, blank=True, null=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name = "Documento Geográfico"
		verbose_name_plural = "Documentos Geográficos"