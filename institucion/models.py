#-*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Institucion(models.Model):
	institucion = models.CharField(max_length=140)

	def __unicode__(self):
		return self.institucion

	class Meta:
		verbose_name = "Institucion"
		verbose_name_plural = "Instituciones"