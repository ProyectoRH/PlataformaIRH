# -*- encoding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from django.contrib.auth.models import User
# Create your models here.

class Documento (models.Model):
	titulo = models.CharField(max_length=255)
	descripcion = RedactorField(verbose_name='Descripción del documento', 
									upload_to='static/uploads_ondas/documentos', 
									allow_file_upload = True, 
									allow_image_upload = True)
	archivo = models.FileField(upload_to='static/uploads_ondas/documentos')
	imagen_portada = models.FileField(upload_to='static/uploads_ondas/documentos')
	fecha_subida = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo