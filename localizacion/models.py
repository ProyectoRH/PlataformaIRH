# -*- encoding: utf-8 -*-
from django.db import models

from areatematicas.models import Areatematica
from representacion.models import Representacion
from zona.models import Zona, SubZona

from djgeojson.fields import GeometryField


class Localizacion(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    area_tematica = models.ForeignKey(Areatematica)
    # representacion = models.ForeignKey(Representacion)
    # zona = models.ManyToManyField(Zona)
    # sub_zona = models.ManyToManyField(SubZona)
    geom = GeometryField(verbose_name='Especifique ubicación')
    privado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.titulo