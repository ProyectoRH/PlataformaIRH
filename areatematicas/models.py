# -*- coding: utf-8 -*-
from django.db import models
from nucleo.models import Nucleo
# Create your models here.

class Areatematica(models.Model):

	nucleo = models.ForeignKey(Nucleo, blank=True, null=True)
	nombreArea = models.CharField('Nombre del Área',max_length = 100)
	descripcion = models.TextField('Descripción', max_length = 150)
	
	class Meta:
		verbose_name = "Área temática"
		verbose_name_plural = "Áreas temáticas"
	
	def __unicode__(self):
		return self.nombreArea
