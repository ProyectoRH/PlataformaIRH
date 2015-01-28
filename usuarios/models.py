from django.db import models

from django.contrib.auth.models import User


class Institucion(models.Model):
	institucion = models.CharField(max_length=140)

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
	institucion = models.ForeignKey(Institucion, null=True, blank=True)
	tipo_usuario = models.ForeignKey(TipoUsuario, null=True, blank=True)

	def __unicode__(self):
		return "%s %s - %s" % (self.usuario.first_name, self.usuario.last_name, self.usuario.username)