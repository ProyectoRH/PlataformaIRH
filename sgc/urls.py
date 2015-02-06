from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recursosRH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'sgc.views.home', name='home'),
    url(r'^login/', 'usuarios.views.iniciarSesion'),
    url(r'^registro/', 'usuarios.views.crearUsuario'),
    url(r'^nosotros/', 'sgc.views.nosotros'),
    url(r'^noticias/', include('noticia.urls')),
    url(r'^app/', 'sgc.views.mapas'),
    url(r'^pagina/', include('pagina.urls')),
    # url(r'^ondas/', 'sgc.views.ondas'),
    # url(r'^nucleoIngHidraulica/', 'sgc.views.nucleo_ingHidraulica'),
    # url(r'^nucleoMarino/', 'sgc.views.nucleo_marino'),
    # url(r'^nucleoHidroBiologico/', 'sgc.views.nucleo_hidroBiologico'),
    # url(r'^nucleoSocioEconomico/', 'sgc.views.nucleo_socioEconomico'),

)
