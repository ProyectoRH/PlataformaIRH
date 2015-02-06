from django.shortcuts import render
from .models import Pagina
# Create your views here.

def pagina_detalle(request, pk):
	pagina = Pagina.objects.get(pk = pk)
	return render(request, 'pagina-detalle.html', {'pagina':pagina})