from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recursosRH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^noticiasOndas/', 'NoticiasOndas.views.noticiasListado', name='ListadoNoticias'),
    url(r'^(?P<pk>[\d]+)', 'NoticiasOndas.views.noticiaDetalle'),


)
