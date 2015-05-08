# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

from areatematicas.models import Areatematica
from representacion.models import Representacion
from zona.models import Zona, SubZona
from nucleo.models import Nucleo

from djgeojson.fields import GeometryField
from django.contrib.gis.db import models

class Localizacion(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    area_tematica = models.ForeignKey(Areatematica)
    # representacion = models.ForeignKey(Representacion)
    # zona = models.ManyToManyField(Zona)
    # sub_zona = models.ManyToManyField(SubZona)
    geom = models.PointField(verbose_name='Especifique ubicación')
    privado = models.BooleanField(default=False)
    nucleo = models.ForeignKey(Nucleo, blank=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.titulo