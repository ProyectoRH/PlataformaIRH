# -*- encoding: utf-8 -*-
from django.db import models

from redactor.fields import RedactorField
from usuarios.models import Institucion

# Create your models here.




class Pagina(models.Model):
	EXTERNO = '__blank'
	INTERNO = ''
	TARGET_CHOICES = (
		(EXTERNO, 'Enlace externo'),
		(INTERNO, 'Enlace Interno'),
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
	target = models.CharField(max_length=140, choices=TARGET_CHOICES, default=EXTERNO)
	institucion = models.ForeignKey(Institucion)

	def __unicode__(self):
		return self.titulo_pagina