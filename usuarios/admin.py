from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, TipoUsuario


class ProfileAdmin(admin.ModelAdmin):
	fields = ('usuario', 'institucion', )


admin.site.register(UserProfile, ProfileAdmin)