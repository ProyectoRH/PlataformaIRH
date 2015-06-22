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
    url(r'^nucleo/(?P<pk>[\d]+)', 'sgc.views.nucleo'),
    url(r'^ondas/', 'sgc.views.ondas'),
    url(r'^documentosOndas/', 'DocumentosOndas.views.todosDocumentos'),
    url(r'^paginasOndas/', include('PaginasOndas.urls')),
    url(r'^noticiasOndas/', include('NoticiasOndas.urls')),
    url(r'^imagenesOndas/', include('ImagenesOndas.urls')),
    url(r'^videosOndas/', include('VideosOndas.urls')),

    # Mapa
    url(r'^busqueda/', 'sgc.views.search'),
    url(r'^busquedaArea/', 'sgc.views.busqueda'),
    url(r'^busquedaPoint/', 'sgc.views.search_point'),
    url(r'^listarMediciones/(?P<localId>[\d]+)', 'sgc.views.listarMediciones'),

    url(r'^getValoresMedicion/', 'sgc.views.getValoresMedicion'),    

)
