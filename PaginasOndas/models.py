# -*- encoding: utf-8 -*-
from django.db import models

from redactor.fields import RedactorField
from usuarios.models import Institucion

from django.contrib.auth.models import User

# Create your models here.

class PaginaOndas(models.Model):
	EXTERNO = '__blank'
	INTERNO = ''
	TARGET_CHOICES = (
		('1', 'Enlace Interno'),
		('2', 'Enlace externo'),
		
	)

	titulo_pagina = models.CharField(max_length=1000)
	cuerpo_pagina = RedactorField(verbose_name='Contenido de la página', 
									upload_to='static/uploads_ondas/paginas', 
									allow_file_upload = True, 
									allow_image_upload = True)
	titulo_menu = models.CharField(max_length=255)
	descripcion = models.TextField()
	pagina_padre = models.ForeignKey("PaginaOndas", blank=True, null=True, default=None)
	peso = models.IntegerField(default=0)
	target = models.CharField(max_length=140, blank=True, null=True, choices=TARGET_CHOICES, default=1)
	url = models.TextField(default=None, blank=True, null=True)
	#institucion = models.ForeignKey(Institucion, blank=True, null=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo_pagina