from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django import template
from pagina.models import Pagina
from noticia.models import Noticia
from usuarios.models import Institucion, UserProfile
from DocumentosOndas.models import Documento
from NoticiasOndas.models import NoticiaOndas
from PaginasOndas.models import PaginaOndas
from VideosOndas.models import VideosOndas
from ImagenesOndas.models import ImagenesOndas
from PaginasOndas.models import PaginaOndas

from areatematicas.models import Areatematica
from documentos_digitales.models import DocumentoDigital

from eventos.models import Evento
from django.contrib.auth.models import User
# Create your views here.

def home(request):
	paginas = []
	paginas_user = Pagina.objects.all()

	for pagina in paginas_user:
		if pagina.usuario.is_superuser and pagina.institucion == None:
			paginas.append(pagina)

	print paginas
	nucleos = Institucion.objects.all()[:4]
	noticias = Noticia.objects.all().order_by('-pk')[:3]
	paginas_ondas = PaginaOndas.objects.all()
	imagenes_ondas = ImagenesOndas.objects.all().order_by('-pk')[:4]
	eventos = Evento.objects.all().order_by('-pk')[:3]
	return render_to_response('index.html', {'paginas':paginas, 'nucleos': nucleos, 'noticias':noticias, 'paginas_ondas':paginas_ondas, 'eventos':eventos, 'imagenes_ondas':imagenes_ondas}, context_instance = RequestContext(request))

def login_sgc(request):
	return render(request, 'login-sgc.html', {})

def nosotros(request):
	return render(request,'nosotros.html',{})

def nucleo(request, pk):
	nucleo_data = Institucion.objects.get(pk = pk)
	usuarios_profiles = UserProfile.objects.filter(institucion = nucleo_data)
	
	paginas = []
	paginas_nucleo = Pagina.objects.filter(institucion = nucleo_data)
	for pagina in paginas_nucleo:
		if pagina.pagina_padre == None:
			paginas.append(pagina)

	contador = 0
		
	noticias = Noticia.objects.filter(institucion = nucleo_data).order_by('-pk')[:12]
	eventos = Evento.objects.filter(institucion = nucleo_data).order_by('-fecha_inicio')[:4]

	#print usuarios_profiles.usuario
	
	print "print de pagina"
	print paginas
	#paginas.append(pagina)

	return render(request, 'nucleo.html', {'nucleo':nucleo_data, 'paginas':paginas, 'contador':contador, 'noticias':noticias, 'eventos':eventos})

def ondas(request):
	documentos = Documento.objects.all().order_by('-pk')[:3]
	noticias = NoticiaOndas.objects.all()[:3]
	paginas = PaginaOndas.objects.all()
	videos = VideosOndas.objects.all()[:1]
	imagenes = ImagenesOndas.objects.all()[:1]

	return render(request,'ondas.html',{'documentos':documentos, 'noticias':noticias, 'paginas':paginas, 'imagen':imagenes, 'video':videos})


def mapas(request):
	areas = Areatematica.objects.all()
	
	return render(request,'index-mapa.html',{'areasTematicas': areas})
	
@csrf_exempt
def busqueda(request):
	if request.method == 'POST':
		valor_busqueda = request.POST.get("busqueda_valor")

		documentos = DocumentoDigital.objects.filter(titulo__contains = valor_busqueda) or DocumentoDigital.objects.filter(resumen__contains = valor_busqueda)
		
		response = ""
		if len(documentos) > 0:
			comboDoc = []
			for documento in documentos:
				dictDoc = {}
				dictDoc['id'] = documento.pk
				dictDoc['titulo'] = documento.titulo
				dictDoc['resumen'] = documento.resumen
				dictDoc['archivo'] = str(documento.archivo)
				dictDoc['geometria'] = documento.localizacion.geom

				comboDoc.append(dictDoc)
				

		return JsonResponse(comboDoc, safe=False)
	else:
		return HttpResponse(0)










