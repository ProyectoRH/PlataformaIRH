# -*- encoding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Usuario
from institucion.models import Institucion




class IniciarSesion(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(IniciarSesion, self).__init__(*args, **kwargs)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		self.user_cache = authenticate(username=username, password=password)

		if self.user_cache is None:
			raise forms.ValidationError(u'Usuario Incorrecto')
		elif not self.user_cache.is_active:
			raise forms.ValidationError(u'Usuario Inactivo')

		return self.cleaned_data

	def getUser(self):
		return self.user_cache



class CrearUsuario(UserCreationForm):
	email = forms.EmailField(max_length=255)
	class Meta:
		model = Usuario
		fields = ('first_name', 'last_name', 'username', 'email', )

	def clean_email(self):
		email = self.cleaned_data.get('email')
		username = self.cleaned_data.get('username')
		if email and Usuario.objects.filter(email=email).exclude(username=username).count():
			raise forms.ValidationError(u'Este email ya se encuentra registrado.')
		return email