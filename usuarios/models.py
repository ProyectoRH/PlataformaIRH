from django.db import models

from django.contrib.auth.models import AbstractUser
from institucion.models import Institucion


class Usuario(AbstractUser):
    """User with app settings."""
    institucion = models.ForeignKey(Institucion, null=True)