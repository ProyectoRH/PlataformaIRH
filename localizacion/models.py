# -*- encoding: utf-8 -*-
from django.db import models

from areatematicas.models import Areatematica
from representacion.models import Representacion
from zona.models import Zona, SubZona

from djgeojson.fields import GeometryField

from smart_selects.db_fields import ChainedForeignKey


class Localizacion(models.Model):
	titulo = models.CharField(max_length=200)
	area_tematica = models.ForeignKey(Areatematica)
	representacion = models.ForeignKey(Representacion)
	zona = models.ManyToManyField(Zona)
	sub_zona = models.ManyToManyField(SubZona)
	geom = GeometryField(verbose_name='Especifique ubicación')


	def __unicode__(self):
		return self.titulo