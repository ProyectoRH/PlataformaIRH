from django.db import models

from areatematicas.models import Areatematica
from representacion.models import Representacion
from zona.models import Zona, SubZona


class Localizacion(models.Model):
	area_tematica = models.ForeignKey(Areatematica)
	representacion = models.ForeignKey(Representacion)
	zona = models.ManyToManyField(Zona)
	sub_zona = models.ManyToManyField(SubZona)


	def __unicode__(self):
		return self.area_tematica