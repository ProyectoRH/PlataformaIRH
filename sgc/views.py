from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django import template
from pagina.models import Pagina
from noticia.models import Noticia
from nucleo.models import Nucleo
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

from Mediciones.models import Medicion, Valores

from eventos.models import Evento
from django.contrib.auth.models import User

import re
from django.db.models import Q

from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
import datetime

# Create your views here.

def home(request):
	paginas = []
	paginas_user = Pagina.objects.all()

	for pagina in paginas_user:
		if pagina.usuario.is_superuser and pagina.nucleo == None:
			paginas.append(pagina)

	nucleos = Nucleo.objects.all()[:4]

	noticias = Noticia.objects.all().order_by('-pk')[:3]
	paginas_ondas = PaginaOndas.objects.all()
	imagenes_ondas = ImagenesOndas.objects.all().order_by('-pk')[:4]
	eventos = Evento.objects.all().order_by('-pk')[:3]
	return render_to_response('index.html', {'paginas':paginas, 'nucleos': nucleos, 'noticias':noticias, 'paginas_ondas':paginas_ondas, 'eventos':eventos, 'imagenes_ondas':imagenes_ondas}, context_instance = RequestContext(request))

def login_sgc(request):
	return render(request, 'login-sgc.html', {})

def nosotros(request):
	return render(request,'nosotros.html',{})

def listarMediciones(request, localId):

	mediciones = Medicion.objects.filter(localizacion = Localizacion.objects.get(pk = localId))
	return render(request, 'listar-medicionesAdmin.html', {'mediciones':mediciones, 'localizacionId':localId})

def nucleo(request, pk):
	nucleo_data = Nucleo.objects.get(pk = pk)
	
	paginas = []
	paginas_nucleo = Pagina.objects.filter(nucleo = nucleo_data)
	for pagina in paginas_nucleo:
		if pagina.pagina_padre == None:
			paginas.append(pagina)

	contador = 0
		
	noticias = Noticia.objects.filter(nucleo = nucleo_data).order_by('-pk')[:12]
	eventos = Evento.objects.filter(nucleo = nucleo_data).order_by('-fecha_inicio')[:4]

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
			dictLoc['geometria'] = str(localizacion.geom)
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
		mediciones_query = get_query(query_string, ['titulo',])

		documentos = DocumentoDigital.objects.filter(entry_query, privado=False)
		localizaciones = Localizacion.objects.filter(entry_query, privado=False)
		doc_shapes = DocumentoShape.objects.filter(shape_query, privado=False)

		doc_shapes_all = DocumentoShape.objects.all()
		documentos_all = DocumentoDigital.objects.all()

		mediciones = Medicion.objects.filter(mediciones_query, privado=False)
		
		comboLoc = []
		comboDoc = []
		comboDocShp = []

		if len(localizaciones) >= 0:
			for localizacion in localizaciones:
				print localizacion.geom
				dictLoc = {}
				dictLoc['id'] = localizacion.pk
				dictLoc['titulo'] = localizacion.titulo
				dictLoc['resumen'] = localizacion.resumen
				dictLoc['geometria'] = str(localizacion.geom)
				dictLoc['locDoc'] = []
				for doc in DocumentoDigital.objects.filter(localizacion = localizacion):
					dictLoc['locDoc'].append(str(doc.archivo))

				dictLoc['locDocShp'] = []
				for doc in DocumentoShape.objects.filter(localizacion = localizacion):
					dictLoc['locDocShp'].append(str(doc.archivo))

				dictLoc['locMed'] = []
				for med in Medicion.objects.filter(localizacion = localizacion):
					dictLoc['locMed'].append("%s ~ %s" % (med.id, med.titulo))

				comboLoc.append(dictLoc)


			for documento in documentos:
				if not documento.localizacion in localizaciones:
					dictDoc = {}
					dictDoc['id'] = documento.localizacion.pk
					dictDoc['titulo'] = documento.localizacion.titulo
					dictDoc['resumen'] = documento.localizacion.resumen
					dictDoc['geometria'] = str(documento.localizacion.geom)
					dictDoc['archivo'] = str(documento.archivo)

					comboDoc.append(dictDoc)

			for documento in doc_shapes:
				if not documento.localizacion in localizaciones:
					dictShp = {}
					dictShp['id'] = documento.localizacion.pk
					dictShp['titulo'] = documento.localizacion.titulo
					dictShp['resumen'] = documento.localizacion.resumen
					dictShp['geometria'] = str(documento.localizacion.geom)
					dictShp['archivo'] = str(documento.archivo)

					comboDocShp.append(dictShp)

			conjuntoArrays = []
			conjuntoArrays.append(comboLoc)
			conjuntoArrays.append(comboDoc)
			conjuntoArrays.append(comboDocShp)

			return JsonResponse(conjuntoArrays, safe=False)
		else:
			return HttpResponse(0)

@csrf_exempt
def search_point(request):
	query_string = ''
	documentos = None

	if ('busqueda_valor' in request.POST) and request.POST['busqueda_valor'].strip():
		query_string = request.POST['busqueda_valor']
		kilometro = request.POST['rango_busqueda']
		string_busqueda = request.POST['string_busqueda']
		try:
			kilometro = int(kilometro)
		except:
			kilometro = 50
		#POINT(-104.590948 38.319914)
		print query_string

		pnt = GEOSGeometry('SRID=4326;%s' % (query_string))
		#qs = Localizacion.objects.filter(geom__contains=pnt)
		#qs = Localizacion.objects.distance(pnt)
		documentos = ""
		doc_shapes = ""
		entry_query = ""
		shape_query = ""
		if string_busqueda != "" and string_busqueda != None and string_busqueda != " ":
			entry_query = get_query(string_busqueda, ['titulo', 'resumen',])
			qs = Localizacion.objects.filter(entry_query, privado=False, geom__distance_lte=(pnt, D(km=kilometro)))
			
			shape_query = get_query(string_busqueda, ['nombre',])
			mediciones_query = get_query(string_busqueda, ['titulo',])

			documentos = DocumentoDigital.objects.filter(entry_query, privado=False)
			doc_shapes = DocumentoShape.objects.filter(shape_query, privado=False)
			mediciones = Medicion.objects.filter(mediciones_query, privado=False)
		else:
			qs = Localizacion.objects.filter(geom__distance_lte=(pnt, D(km=kilometro)))

		

		print qs
		print documentos
		print doc_shapes
		comboLoc = []
		if len(qs) > 0:
			comboLoc = []
			comboDoc = []
			comboDocShp = []
			comboMediciones = []

			for localizacion in qs:
				dictLoc = {}
				dictLoc['id'] = localizacion.pk
				dictLoc['titulo'] = localizacion.titulo
				dictLoc['resumen'] = localizacion.resumen
				dictLoc['geometria'] = str(localizacion.geom)
				dictLoc['locDoc'] = []
				
				for doc in DocumentoDigital.objects.filter(localizacion = localizacion):
					dictLoc['locDoc'].append(str(doc.archivo))

				dictLoc['locDocShp'] = []
				for doc in DocumentoShape.objects.filter(localizacion = localizacion):
					dictLoc['locDocShp'].append(str(doc.archivo))

				dictLoc['locMed'] = []
				for med in Medicion.objects.filter(localizacion = localizacion):
					dictLoc['locMed'].append("%s ~ %s" % (med.id, med.titulo))

				comboLoc.append(dictLoc)

			if len(documentos) > 0:
				for documento in documentos:
					if not documento.localizacion in qs:
						dictDoc = {}
						dictDoc['id'] = documento.localizacion.pk
						dictDoc['titulo'] = documento.localizacion.titulo
						dictDoc['resumen'] = documento.localizacion.resumen
						dictDoc['geometria'] = str(documento.localizacion.geom)
						dictDoc['archivo'] = str(documento.archivo)

						comboDoc.append(dictDoc)

			if len(doc_shapes) > 0:
				for documento in doc_shapes:
					if not documento.localizacion in qs:
						dictShp = {}
						dictShp['id'] = documento.localizacion.pk
						dictShp['titulo'] = documento.localizacion.titulo
						dictShp['resumen'] = documento.localizacion.resumen
						dictShp['geometria'] = str(documento.localizacion.geom)
						dictShp['archivo'] = str(documento.archivo)

						comboDocShp.append(dictShp)

			conjuntoArrays = []
			conjuntoArrays.append(comboLoc)
			conjuntoArrays.append(comboDoc)
			conjuntoArrays.append(comboDocShp)

			return JsonResponse(conjuntoArrays, safe=False)
		else:
			return HttpResponse(0)

@csrf_exempt
def getValoresMedicion(request):
	if request.method == 'POST':
		idValor = request.POST["idMedicion"]

		medicionObj = Medicion.objects.get(pk = idValor)
		valoresMedicion = Valores.objects.filter(medicion = medicionObj).order_by('pk')

		comboValores = []

		for valor in valoresMedicion:
			dictValores = {}
			dictValores["valor"] = valor.valor_medido
			if medicionObj.periodo == "anio":
				dictValores["fecha"] = valor.fecha.strftime('%Y')
			elif medicionObj.periodo == "mes":
				dictValores["fecha"] = valor.fecha.strftime('%m')
			elif medicionObj.periodo == "dia":
				dictValores["fecha"] = valor.fecha.strftime('%d')

			comboValores.append(dictValores)

		return JsonResponse(comboValores, safe=False)





