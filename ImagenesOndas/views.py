from django.shortcuts import render
from .models import ImagenesOndas

# Create your views here.

def galeriaImagenes(request):
	imagenes = ImagenesOndas.objects.all()

	return render(request, 'ondas_imagenes.html', {'imagenes':imagenes})