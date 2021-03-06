# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from localizacion.models import Localizacion
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
	oeste = models.CharField(max_length=140, blank=True)
	este = models.CharField(max_length=140, blank=True)
	norte = models.CharField(max_length=140, blank=True)
	sur = models.CharField(max_length=140, blank=True)
	nivel = models.ForeignKey(Nivel)
	archivo = models.FileField(upload_to = "static/documentos_digitales/")
	localizacion = models.ForeignKey(Localizacion, null=True)
	privado = models.BooleanField(default=False)

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name = "Documento Digital"
		verbose_name_plural = "Documentos Digitales"
