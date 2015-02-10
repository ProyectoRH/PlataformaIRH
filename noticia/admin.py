from django.contrib import admin

# Register your models here.
from .models import Noticia
from usuarios.models import UserProfile


class NoticiaAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
		perfil = UserProfile.objects.get(usuario = request.user)
		obj.institucion = perfil.institucion
		obj.save()


admin.site.register(Noticia, NoticiaAdmin)