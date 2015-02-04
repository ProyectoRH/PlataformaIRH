from django.shortcuts import render
from .forms import IniciarSesion
from django.http import HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate

# Create your views here.
def iniciarSesion(request):
	form = IniciarSesion(request.POST or None)
	
	if request.user.is_authenticated():
		if request.user.is_staff:
			HttpResponseRedirect('/admin/')
		return HttpResponseRedirect('/')

	if form.is_valid():
		login(request, form.getUser())
		if request.user.is_staff:
			HttpResponseRedirect('/admin/')

		return HttpResponseRedirect('/')
	
	
	return render(request, 'login-sgc.html', {
		'form': form,
	})