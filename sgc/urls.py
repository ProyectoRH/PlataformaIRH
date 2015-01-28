from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recursosRH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'sgc.views.home', name='home'),
    url(r'^nosotros/', 'sgc.views.nosotros'),
    url(r'^noticias/', 'sgc.views.noticias'),
    url(r'^historicas/', 'sgc.views.noticias_historicas'),
    url(r'^ondas/', 'sgc.views.ondas'),
    url(r'^nucleoIngHidraulica/', 'sgc.views.nucleo_ingHidraulica'),
    url(r'^nucleoMarino/', 'sgc.views.nucleo_marino'),
    url(r'^nucleoHidroBiologico/', 'sgc.views.nucleo_hidroBiologico'),
    url(r'^nucleoSocioEconomico/', 'sgc.views.nucleo_socioEconomico'),

)
