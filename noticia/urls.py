from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recursosRH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'noticia.views.noticias', name='homeNoticias'),
    url(r'^historicas/', 'noticia.views.noticias_historicas', name='homeNoticias'),
    url(r'^noticia/(?P<pk>[\d]+)', 'noticia.views.noticias', name='homeNoticias'),
    # url(r'^ondas/', 'sgc.views.ondas'),
    # url(r'^nucleoIngHidraulica/', 'sgc.views.nucleo_ingHidraulica'),
    # url(r'^nucleoMarino/', 'sgc.views.nucleo_marino'),
    # url(r'^nucleoHidroBiologico/', 'sgc.views.nucleo_hidroBiologico'),
    # url(r'^nucleoSocioEconomico/', 'sgc.views.nucleo_socioEconomico'),

)
