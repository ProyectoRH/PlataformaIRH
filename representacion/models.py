from django.db import models


class Representacion(models.Model):
	nombre = models.CharField(max_length=140)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre