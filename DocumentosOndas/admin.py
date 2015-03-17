from django.contrib import admin
from .models import Documento
# Register your models here.

class DocumentosAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
    	if not request.user.is_superuser:
			obj.usuario = request.user
			obj.save()

admin.site.register(Documento, DocumentosAdmin)