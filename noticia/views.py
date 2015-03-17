from django.shortcuts import render
from .models import Noticia
# Create your views here.

def noticias(request):
	noticias = Noticia.objects.all()
	return render(request,'noticias.html',{'noticias':noticias})

def noticia_detalle(request, pk):
	noticia = Noticia.objects.get(pk = pk);
	return render(request, 'noticia-detalle.html',{'noticia': noticia,})

def noticias_historicas(request):
	return render(request,'historicas.html',{})