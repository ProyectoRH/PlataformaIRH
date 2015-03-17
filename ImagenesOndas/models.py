# -*- encoding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
# Create your models here.

class ImagenesOndas(models.Model):
	titulo = models.CharField(max_length=255)
	descripcion = RedactorField(verbose_name='Descripción de imagen', 
									upload_to='static/upload_ondas/imagenes', 
									allow_file_upload = True, 
									allow_image_upload = True)
	imagen = models.FileField(upload_to='static/upload_ondas/imagenes')

	def __unicode__(self):
		return self.titulo