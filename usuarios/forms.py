# -*- encoding:utf-8 -*-
from django import forms


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