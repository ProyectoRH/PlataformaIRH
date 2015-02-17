from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, Institucion, TipoUsuario


# Se define un inline para el admin de UserProfile
class ProfileInline(admin.StackedInline):
    model = UserProfile
    fields = ('institucion', )
    can_delete = False
    verbose_name = 'Perfil de Usuario'
    verbose_name_plural = 'Perfiles de Usuarios'


# Se define un nuevo UserAdmin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def save_formset(self, request, form, formset, change):
        formset.save()
        if not change:
        	perfil = UserProfile.objects.get(usuario = request.user)
        	for f in formset.forms:
				obj = f.instance 
				obj.institucion = perfil.institucion
				obj.save()


class ProfileAdmin(admin.ModelAdmin):
	fields = ('usuario', 'institucion', )


# Re-registra UserAdmin
admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Institucion)
admin.site.register(TipoUsuario)
admin.site.register(UserProfile, ProfileAdmin)