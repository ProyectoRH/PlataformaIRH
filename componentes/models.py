# -*- coding: utf-8 -*-
from django.db import models
from areatematicas.models import Areatematica

# Create your models here.

class Componente (models.Model):

	CM_nomComp = models.CharField('Nombre del Componente',max_length = 100)
	CM_descrip = models.TextField('Descripción', max_length	 = 150)
        areatematica = models.ForeignKey(Areatematica)

	
	class Meta:
		verbose_name = "Componente"
		verbose_name_plural = "Componentes"
