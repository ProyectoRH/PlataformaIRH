from django.contrib import admin

# Register your models here.
from .models import EventoOndas
from usuarios.models import UserProfile


class EventoAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
		perfil = UserProfile.objects.get(usuario = request.user)
		obj.institucion = perfil.institucion
		obj.save()


admin.site.register(EventoOndas, EventoAdmin)