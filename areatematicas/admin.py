from django.contrib import admin

# Register your models here.
from areatematicas.models import Areatematica
from nucleo.models import Nucleo

class AreatematicaAdmin(admin.ModelAdmin):
	
	def get_form(self, request, obj=None, **kwargs):
		self.exclude = []
		if not request.user.is_superuser:
			self.exclude.append('nucleo')
		return super(AreatematicaAdmin, self).get_form(request, obj, **kwargs)
	
	def save_model(self, request, obj, form, change):
		try:
			nucleo = Nucleo.objects.get(institucion = request.user.institucion)
			obj.nucleo = nucleo
			obj.save()
		except:
			pass

admin.site.register(Areatematica, AreatematicaAdmin)
