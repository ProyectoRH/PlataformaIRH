from django.contrib import admin
from .models import Medicion, Valores
from django.http import HttpResponse
# Register your models here.

class ValoresInline(admin.StackedInline):
	model = Valores
	extra = 1

class MedicionAdmin(admin.ModelAdmin):
	inlines = [ValoresInline,]

	def response_change(self, request, obj, post_url_continue='../%s/'):
		resp = super(MedicionAdmin, self).response_change(request, obj)
		if request.POST.has_key("_popup"):
			return HttpResponse('<script type="text/javascript">window.close();window.opener.location.reload(true);</script>')# % \
				#(escape(obj._get_pk_val()),escape(obj)))
		return resp 

	@property
	def media(self):
		media = super(MedicionAdmin, self).media
		js = ["js/testMediciones.js",]
		media.add_js(js)
		return media

admin.site.register(Medicion, MedicionAdmin)