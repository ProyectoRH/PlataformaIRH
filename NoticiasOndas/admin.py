from django.contrib import admin

# Register your models here.
from .models import NoticiaOndas


class NoticiaAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()


admin.site.register(NoticiaOndas, NoticiaAdmin)