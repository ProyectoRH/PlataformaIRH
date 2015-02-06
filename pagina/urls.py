from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recursosRH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'noticia.views.noticias', name='homeNoticias'),
    url(r'^(?P<pk>[\d]+)', 'pagina.views.pagina_detalle', name='paginaDetalle'),
    
)
