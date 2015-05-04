# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from localizacion.models import Localizacion
from usuarios.models import Institucion
from nucleo.models import Nucleo


class Idioma(models.Model):
	idioma = models.CharField(max_length=140)

	def __unicode__(self):
		return self.idioma


class Nivel(models.Model):
	nivel = models.CharField(max_length=200)

	def __unicode__(self):
		return self.nivel




class DocumentoDigital(models.Model):
	titulo = models.CharField(max_length=200)
	fecha_creacion = models.DateField("Fecha de creación")
	resumen = models.TextField()
	denominador = models.CharField(max_length=200)
	idioma = models.ForeignKey(Idioma)
	oeste = models.CharField(max_length=140)
	este = models.CharField(max_length=140)
	norte = models.CharField(max_length=140)
	sur = models.CharField(max_length=140)
	nivel = models.ForeignKey(Nivel)
	nucleo = models.ForeignKey(Nucleo, blank=True, null=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
	archivo = models.FileField(upload_to = "static/documentos_digitales/")
	localizacion = models.ForeignKey(Localizacion, null=True)
	privado = models.BooleanField(default=False)

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name = "Documento Digital"
		verbose_name_plural = "Documentos Digitales"