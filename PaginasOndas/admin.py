from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import PaginaOndas
from usuarios.models import UserProfile


class PaginaAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
    	if not request.user.is_superuser:
			obj.usuario = request.user
			obj.save()


admin.site.register(PaginaOndas, PaginaAdmin)