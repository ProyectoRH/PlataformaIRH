from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Pagina
from usuarios.models import UserProfile


class PaginaAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
		perfil = UserProfile.objects.get(usuario = request.user)
		obj.institucion = perfil.institucion
		obj.save()


admin.site.register(Pagina, PaginaAdmin)