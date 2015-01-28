#encoding:utf-8
"""
Django settings for recursosRH project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i4=i+p$k8(_6ehr^taa+ajg_%m(r%eegp#0h%0w3(pyfnd^#+&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'redactor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'sgc',
    'areatematicas',
    'componentes',
    'subcomponentes',
    'factor',
    'categorias',
    'usuarios',
    'pagina',
    'eventos',
    'noticia',
    'portada',
    'representacion',
    'smart_selects',
    'zona',
    'localizacion',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'recursosRH.urls'

WSGI_APPLICATION = 'recursosRH.wsgi.application'

STATICFILES_FINDERS = (
   'django.contrib.staticfiles.finders.AppDirectoriesFinder', 
   'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP+( 
   'django.core.context_processors.request',
   'django.contrib.auth.context_processors.auth',
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'recursosdb',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'recursosrh',
            'PASSWORD': 'nmveaviieotf',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }

POSTGIS_VERSION = (2, 0, 3)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REDACTOR_OPTIONS = {'lang': 'es'}
REDACTOR_UPLOAD = '/static/uploads/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content'])

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = ('templates',)


SUIT_CONFIG={
	'ADMIN_NAME': 'PLATAFORMA DE RECURSOS HIDRICOS DEL ATLANTICO',
	'MENU':(
		'sites',
		{'label': u'Gestión de Usuarios', 'icon': 'icon-user','models':('auth.user','auth.group')},
		{'label': u'Gestión de Filtros', 'icon': 'icon-search','models':({'label':'Area Tematica','url':'/admin/areatematicas/'},{'label':'Componentes','url':'/admin/componentes/'},{'label':'Sub-Componentes','url':'/admin/subcomponentes/'},{'label':'Factores','url':'/admin/factor/'},)},
		{'label': u'Gestión de Contenidos', 'icon': 'icon-book','models':({'label':'Ficheros','url':'/admin/documentos/'},{'label':'Crear páginas','url':'/admin/pagina/'},{'label':'Crear Noticias','url':'/admin/noticia/'},{'label':'Crear Eventos','url':'/admin/eventos/'},)},
		{'label': u'Ondas', 'icon': 'icon-volume-up','models':({'label':'Noticias','url':'/admin/notiondas/'},{'label':'Eventos','url':'/admin/eventoondas/'},{'label':'Paginas','url':'/admin/paginaondas/'},)},
		
	)

}
