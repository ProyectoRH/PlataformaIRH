from django.db import models

from django.contrib.auth.models import User


class Pais(models.Model):
	pais = models.CharField(max_length=200)

	def __unicode__(self):
		return self.pais


class Ciudad(models.Model):
	ciudad = models.CharField(max_length=200)

	def __unicode__(self):
		return self.ciudad


class Institucion(models.Model):
	institucion = models.CharField(max_length=140)
	nombre_nucleo = models.CharField(max_length=255)
	imagen_banner = models.ImageField(upload_to = "static/uploads_nucleos/banner_images", null = True)
	descripcion_nucleo = models.TextField()
	logo_institucion = models.ImageField(upload_to = "static/logo_instituciones", null = True)

	def __unicode__(self):
		return self.institucion

	class Meta:
		verbose_name = "Institucion"
		verbose_name_plural = "Instituciones"


class TipoUsuario(models.Model):
	tipo_usuario = models.CharField(max_length=140)

	def __unicode__(self):
		return self.tipo_usuario



class UserProfile(models.Model):
	usuario = models.OneToOneField(User)
	institucion = models.ForeignKey(Institucion, null=True, blank=True, default=None)
	tipo_usuario = models.ForeignKey(TipoUsuario, null=True, blank=True)
	funcion = models.CharField(max_length=200, blank=True, null=True)
	pais = models.ForeignKey(Pais, null=True)
	ciudad = models.ForeignKey(Ciudad, null=True)

	def __unicode__(self):
		return "%s %s - %s" % (self.usuario.first_name, self.usuario.last_name, self.usuario.username)
