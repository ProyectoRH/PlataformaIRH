# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

from redactor.fields import RedactorField

from nucleo.models import Nucleo
from django.contrib.auth.models import User

# Create your models here.

class Pagina(models.Model):
	EXTERNO = '__blank'
	INTERNO = ''
	TARGET_CHOICES = (
		('1', 'Enlace Interno'),
		('2', 'Enlace externo'),
		
	)

	titulo_pagina = models.CharField(max_length=1000)
	cuerpo_pagina = RedactorField(verbose_name='Contenido de la página', 
									upload_to='static/uploads_paginas', 
									allow_file_upload = True, 
									allow_image_upload = True)
	titulo_menu = models.CharField(max_length=255)
	descripcion = models.TextField()
	pagina_padre = models.ForeignKey("Pagina", blank=True, null=True, default=None)
	peso = models.IntegerField(default=0)
	target = models.CharField(max_length=140, blank=True, null=True, choices=TARGET_CHOICES, default=1)
	url = models.TextField(default=None, blank=True, null=True)
	nucleo = models.ForeignKey(Nucleo, blank=True, null=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.titulo_pagina
