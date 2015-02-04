from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html',{})

def nosotros(request):
	return render(request,'nosotros.html',{})	
def noticias(request):
	return render(request,'noticias.html',{})
def noticias_historicas(request):
	return render(request,'historicas.html',{})
# def ondas(request):
# 	return render(request,'ondas.html',{})

# def nucleo_ingHidraulica(request):
# 	return render(request,'nucleoinghidraulica.html',{})
# def nucleo_marino(request):
# 	return render(request,'nucleomarino.html',{})
# def nucleo_hidroBiologico(request):
# 	return render(request,'nucleorecursoshidrobiologico.html',{})
# def nucleo_socioEconomico(request):
# 	return render(request,'nucleosocioeconomico.html',{})


def mapas(request):
    return render(request,'inicio-mapas.html',{})
