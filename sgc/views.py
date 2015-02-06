from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from pagina.models import Pagina
# Create your views here.

def home(request):
	paginas = Pagina.objects.all()
	return render_to_response('index.html', {'paginas':paginas}, context_instance=RequestContext(request))

def paginas_hijo(self, pk):
	paginas_hijo = Pagina.objects.filter(pagina_padre = pk)

	return paginas_hijo

def login_sgc(request):
	return render(request, 'login-sgc.html', {})

def nosotros(request):
	return render(request,'nosotros.html',{})

# def ondas(request):
# 	return render(request,'ondas.html',{})

# def nucleo_ingHidraulica(request):
# 	return render(request,'nucleoinghidraulica.html',{})
# def nucleo_marino(request):
# 	return render(request,'nucleomarino.html',{})
# def nucleo_hidroBiologico(request):
# 	return render(request,'nucleorecursoshidrobiologico.html',{})
# def nucleo_socioEconomico(request):
# 	return render(request,'nucleosocioeconomico.html',{})


def mapas(request):
    return render(request,'index-mapa.html',{})
