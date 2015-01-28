# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField('Descripción',blank=True,null=True)
 
 	   
    def __str__(self):
        return self.nombre
	
	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"