# -*- encoding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
# Create your models here.

class VideosOndas(models.Model):
	titulo = models.CharField(max_length=255)
	descripcion = RedactorField(verbose_name='Descripcion del video', 
									upload_to='static/upload_ondas/videos', 
									allow_file_upload = True, 
									allow_image_upload = True)
	url_video = models.URLField()

	def __unicode__(self):
		return self.titulo