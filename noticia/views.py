from django.shortcuts import render
from .models import Noticia
from eventos.models import Evento
# Create your views here.

def noticias(request):
	noticias = Noticia.objects.all().order_by('-pk')[:12]
	eventos = Evento.objects.all().order_by('-pk')[:4]
	return render(request,'noticias.html',{'noticias':noticias, 'eventos':eventos})

def noticia_detalle(request, pk):
	noticia = Noticia.objects.get(pk = pk)
	return render(request, 'noticia-detalle.html',{'noticia': noticia,})

def noticias_historicas(request):
	return render(request,'historicas.html',{})