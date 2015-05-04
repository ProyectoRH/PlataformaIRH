from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Pagina
from django.contrib.auth.models import User

class PaginaAdmin(admin.ModelAdmin):
	exclude = ('usuario', 'institucion')

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()


admin.site.register(Pagina, PaginaAdmin)