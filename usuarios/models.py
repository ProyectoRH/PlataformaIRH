#-*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

from django.contrib.auth.models import User, UserManager

from institucion.models import Institucion
from nucleo.models import Nucleo


class Usuario(User):
    """User with app settings."""
    nucleo = models.ForeignKey(Nucleo, blank=True, null=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()