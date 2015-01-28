# -*- coding: utf-8 -*-
from django.db import models
from componentes.models import Componente
# Create your models here.

class Subcomponente (models.Model):

	SC_nomSubcomp = models.CharField('Nombre del Subcomponente',max_length = 100)
	SC_descrip = models.TextField('Descripción', max_length = 150)
	componente = models.ForeignKey(Componente)
	
	class Meta:
		verbose_name = "Subcomponente"
		verbose_name_plural = "Subcomponentes"
