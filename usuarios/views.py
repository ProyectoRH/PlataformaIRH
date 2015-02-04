from django.shortcuts import render
from .forms import IniciarSesion
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
	crear_perfil = CrearPerfil(request.POST or None, prefix = "perfil")

	if crear_usuario.is_valid() and crear_perfil.is_valid():
		usuario = crear_usuario.save()

		perfil = crear_perfil.save(commit = False)

		perfil.usuario = usuario
		perfil.save()

	return render(request, 'crear-usuario.html', {
		'crear_usuario': crear_usuario,
		'crear_perfil': crear_perfil,
	})