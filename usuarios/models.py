#-*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

from django.contrib.auth.models import User, UserManager

from institucion.models import Institucion
from nucleo.models import Nucleo


class Usuario(User):
    """User with app settings."""
    institucion = models.ForeignKey(Institucion)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()