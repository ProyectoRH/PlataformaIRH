# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from subcomponentes.models import Subcomponente

# Create your models here.

class Factor (models.Model):

	FC_nomFactor = models.CharField('Nombre del Factor',max_length = 100)
	FC_descrip = models.TextField('Descripción', max_length	 = 150)
        subcomponente = models.ForeignKey(Subcomponente)

	
	class Meta:
		verbose_name = "Factor"
		verbose_name_plural = "Factores"
