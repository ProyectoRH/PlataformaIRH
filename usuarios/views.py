from django.shortcuts import render
from .forms import IniciarSesion, CrearUsuario
from django.http import HttpResponseRedirect

from django.contrib.auth import login, authenticate

# Create your views here.
def iniciarSesion(request):
	form = IniciarSesion(request.POST or None)
	
	if request.user.is_authenticated():
		if request.user.is_staff:
			return HttpResponseRedirect('/admin/')
		return HttpResponseRedirect('/')

	if form.is_valid():
		login(request, form.getUser())
		if request.user.is_staff:
			return HttpResponseRedirect('/admin/')
		else:
			return HttpResponseRedirect('/')
	
	
	return render(request, 'login-sgc.html', {
		'form': form,
	})



def crearUsuario(request):
	crear_usuario = CrearUsuario(request.POST or None, prefix = "usuario")

	if crear_usuario.is_valid():
		usuario = crear_usuario.save()

		return HttpResponseRedirect('/')

	return render(request, 'registro-sgc.html', {
		'crear_usuario': crear_usuario,
	})