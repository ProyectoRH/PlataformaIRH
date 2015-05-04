from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from institucion.models import Institucion



class Nucleo(models.Model):
	institucion = models.ForeignKey(Institucion)
	nucleo = models.CharField(max_length=200)
	imagen_banner = models.ImageField(upload_to = "static/uploads_nucleos/banners_nucleos", null = True)
	descripcion = models.TextField()
	imagen_logo = models.ImageField(upload_to = "static/uploads_nucleos/logos_nucleos", null = True)

	def __unicode__(self):
		return self.nucleo