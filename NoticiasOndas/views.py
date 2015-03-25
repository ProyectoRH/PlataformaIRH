from django.shortcuts import render
from .models import NoticiaOndas
# Create your views here.

def noticiaDetalle(request, pk):
	noticia = NoticiaOndas.objects.get(pk = pk)

	return render(request, 'ondas_noticiaDetalle.html', {'noticia':noticia})

def noticiasListado(request):
	noticias = NoticiaOndas.objects.all().order_by('-pk')

	return render(request, 'ondas_noticias.html', {'noticias':noticias})
