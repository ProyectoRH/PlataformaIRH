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
from documentos_shape.models import DocumentoShape
from localizacion.models import Localizacion

from eventos.models import Evento
from django.contrib.auth.models import User

import re
from django.db.models import Q
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
		area_busqueda = request.POST.get("area_busqueda")

		area_tematica = Areatematica.objects.get(pk = area_busqueda)

		localizaciones = Localizacion.objects.filter(area_tematica = area_tematica)
		
		comboLocal = []
		for localizacion in localizaciones:
			dictLoc = {}
			dictLoc['id'] = localizacion.id
			dictLoc['titulo'] = localizacion.titulo
			dictLoc['resumen'] = localizacion.resumen
			dictLoc['geometria'] = localizacion.geom
			dictLoc['locDoc'] = []
			for doc in DocumentoDigital.objects.filter(localizacion = localizacion):
				dictLoc['locDoc'].append(str(doc.archivo))

			dictLoc['locDocShp'] = []
			for doc in DocumentoShape.objects.filter(localizacion = localizacion):
				dictLoc['locDocShp'].append(str(doc.archivo))

			comboLocal.append(dictLoc)

		return JsonResponse(comboLocal, safe=False)
	else:
		return HttpResponse(0)


def normalize_query(query_string,findterms=re.compile(r'"([^"]+)"|(\S+)').findall,normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

@csrf_exempt
def search(request):
	query_string = ''
	documentos = None

	if ('busqueda_valor' in request.POST) and request.POST['busqueda_valor'].strip():
		query_string = request.POST['busqueda_valor']

		entry_query = get_query(query_string, ['titulo', 'resumen',])
		shape_query = get_query(query_string, ['nombre',])

		documentos = DocumentoDigital.objects.filter(entry_query, privado=False)
		localizaciones = Localizacion.objects.filter(entry_query, privado=False)
		doc_shapes = DocumentoShape.objects.filter(shape_query, privado=False)

		doc_shapes_all = DocumentoShape.objects.all()
		documentos_all = DocumentoDigital.objects.all()

		
		comboLoc = []
		comboDoc = []
		comboDocShp = []


		
		if len(localizaciones) > 0:
			for localizacion in localizaciones:
				dictLoc = {}
				dictLoc['id'] = localizacion.pk
				dictLoc['titulo'] = localizacion.titulo
				dictLoc['resumen'] = localizacion.resumen
				dictLoc['geometria'] = localizacion.geom
				dictLoc['locDoc'] = []
				for doc in DocumentoDigital.objects.filter(localizacion = localizacion):
					dictLoc['locDoc'].append(str(doc.archivo))

				dictLoc['locDocShp'] = []
				for doc in DocumentoShape.objects.filter(localizacion = localizacion):
					dictLoc['locDocShp'].append(str(doc.archivo))

				comboLoc.append(dictLoc)


			for documento in documentos:
				if not documento.localizacion in localizaciones:
					dictDoc = {}
					dictDoc['id'] = documento.localizacion.pk
					dictDoc['titulo'] = documento.localizacion.titulo
					dictDoc['resumen'] = documento.localizacion.resumen
					dictDoc['geometria'] = documento.localizacion.geom
					dictDoc['archivo'] = str(documento.archivo)

					comboDoc.append(dictDoc)

			for documento in doc_shapes:
				if not documento.localizacion in localizaciones:
					dictShp = {}
					dictShp['id'] = documento.localizacion.pk
					dictShp['titulo'] = documento.localizacion.titulo
					dictShp['resumen'] = documento.localizacion.resumen
					dictShp['geometria'] = documento.localizacion.geom
					dictShp['archivo'] = str(documento.archivo)

					comboDocShp.append(dictShp)

			conjuntoArrays = []
			conjuntoArrays.append(comboLoc)
			conjuntoArrays.append(comboDoc)
			conjuntoArrays.append(comboDocShp)

			return JsonResponse(conjuntoArrays, safe=False)
		else:
			return HttpResponse(0)







