#encoding:utf-8
from django.db import models
from localizacion.models import Localizacion

# Create your models here.

class Medicion(models.Model):
	titulo = models.CharField(max_length=255)
	unidad_medida = models.CharField(max_length=255)
	descripcion = models.TextField()

	PERIODOS = (
		('anio', "Años"),
		('mes', "Meses"),
		('dia', "Días"),
	)

	periodo = models.CharField(max_length=100, choices=PERIODOS)
	localizacion = models.ForeignKey(Localizacion)
	privado = models.BooleanField(default=False)

	def __unicode__(self):
		return self.titulo

class Valores(models.Model):
	medicion = models.ForeignKey(Medicion)
	valor_medido = models.CharField(max_length=255)
	fecha = models.DateTimeField()

	def __unicode__(self):
		return "%s - %s" % (self.medicion.titulo, self.valor_medido)