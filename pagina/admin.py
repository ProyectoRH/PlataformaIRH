from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Pagina
from usuarios.models import UserProfile
from django.contrib.auth.models import User

class PaginaAdmin(admin.ModelAdmin):
	exclude = ('usuario',)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		if not request.user.is_superuser:
			perfil = UserProfile.objects.get(usuario = request.user)
			obj.institucion = perfil.institucion
			
		obj.save()


admin.site.register(Pagina, PaginaAdmin)