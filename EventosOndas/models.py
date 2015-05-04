# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
# Create your models here.
from redactor.fields import RedactorField


class EventoOndas(models.Model):
	titulo = models.CharField(max_length = 255)
	descripcion = models.TextField()
	cuerpo_evento = RedactorField(verbose_name='Contenido de eventos', 
									upload_to='static/upload_ondas/eventos', 
									allow_file_upload = True, 
									allow_image_upload = True)
	fecha_inicio = models.DateField("Fecha de inicio")
	fecha_final = models.DateField("Fecha de finalización")
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return self.titulo