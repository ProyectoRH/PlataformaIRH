# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
from redactor.fields import RedactorField
from usuarios.models import Institucion

class Evento(models.Model):
	titulo = models.CharField(max_length = 255)
	descripcion = models.TextField()
	cuerpo_evento = RedactorField(verbose_name='Contenido de eventos', 
									upload_to='static/uploads_eventos', 
									allow_file_upload = True, 
									allow_image_upload = True)
	fecha_inicio = models.DateField("Fecha de inicio")
	fecha_final = models.DateField("Fecha de finalización")
	institucion = models.ForeignKey(Institucion, blank=True, null=True)
