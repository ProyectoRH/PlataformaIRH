#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Institucion(models.Model):
	institucion = models.CharField(max_length=140)
	imagen_banner = models.ImageField(upload_to = "static/uploads_nucleos/banner_images", null = True)
	descripcion_nucleo = models.TextField()
	logo_institucion = models.ImageField(upload_to = "static/logo_instituciones", null = True)

	def __unicode__(self):
		return self.institucion

	class Meta:
		verbose_name = "Institucion"
		verbose_name_plural = "Instituciones"