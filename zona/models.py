from django.db import models

from representacion.models import Representacion


class Zona(models.Model):
	representacion = models.ForeignKey(Representacion)
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.titulo



class SubZona(models.Model):
	zona = models.ForeignKey(Zona)
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.titulo