from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Documento
# Create your views here.

def todosDocumentos(request):
	documentos = Documento.objects.all()

	return render_to_response('ondas_masDocumentos.html', {'documentos':documentos}, context_instance = RequestContext(request))