# -*- encoding: utf-8 -*-
from django.db import models

from usuarios.models import Institucion

from redactor.fields import RedactorField

# Create your models here.

class NoticiaOndas(models.Model):
	institucion = models.ForeignKey(Institucion, blank=True, default = None)
	titulo = models.CharField(max_length=255)
	imagen_banner = models.ImageField(upload_to = "static/uploads_noticias/banner_images", blank = True)
	cuerpo_noticia = RedactorField(verbose_name='Contenido de noticias', 
									upload_to='static/uploads_ondas/noticias', 
									allow_file_upload = True, 
									allow_image_upload = True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.titulo