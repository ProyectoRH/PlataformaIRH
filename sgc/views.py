from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import template
from pagina.models import Pagina
from usuarios.models import Institucion, UserProfile
from django.contrib.auth.models import User
# Create your views here.

register = template.Library()

def home(request):
	paginas = None
	# if request.user.username != None:
	# 	if request.user.is_superuser:
	nucleos = Institucion.objects.all()

	
	
	return render_to_response('index.html', {'paginas':paginas, 'nucleos': nucleos}, context_instance = RequestContext(request))

def login_sgc(request):
	return render(request, 'login-sgc.html', {})

def nosotros(request):
	return render(request,'nosotros.html',{})

@register.filter(name="lower")
def lower(value):
    """Removes all values of arg from the given string"""
    return value.lower()

def nucleo(request, pk):
	nucleo_data = Institucion.objects.get(pk = pk)
	usuarios_profiles = UserProfile.objects.filter(institucion = nucleo_data)
	
	contador = 0

	paginas = []
	for usuario in usuarios_profiles:
		pagina = Pagina.objects.filter(usuario = usuario.usuario)	
		paginas.append(pagina)

	

	#print usuarios_profiles.usuario
	
	print "print de pagina"
	print paginas
	#paginas.append(pagina)

	return render(request, 'nucleo.html', {'nucleo':nucleo_data, 'paginas':paginas, 'contador':contador})

def ondas(request):
	return render(request,'ondas.html',{})

# def nucleo_hidroBiologico(request):
# 	return render(request,'nucleorecursoshidrobiologico.html',{})
# def nucleo_socioEconomico(request):
# 	return render(request,'nucleosocioeconomico.html',{})


def mapas(request):
    return render(request,'index-mapa.html',{})
