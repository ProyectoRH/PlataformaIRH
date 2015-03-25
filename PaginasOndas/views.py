from django.shortcuts import render
from .models import PaginaOndas
# Create your views here.

def paginaDetalle(request, pk):
	pagina = PaginaOndas.objects.get(pk = pk)
	return render(request, 'ondas_paginaDetalle.html', {'pagina':pagina})