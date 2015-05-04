#-*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser, UserManager

from institucion.models import Institucion
from nucleo.models import Nucleo
from django.contrib.auth import models as auth_models


class Usuario(AbstractUser):
    """User with app settings."""
    institucion = models.ForeignKey(Institucion, null=True)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()