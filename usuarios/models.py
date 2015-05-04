#-*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings

from django.contrib.auth.models import AbstractUser, UserManager

from institucion.models import Institucion
from nucleo.models import Nucleo
from django.contrib.auth import models as auth_models


class MyUserManager(UserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractUser):
    """User with app settings."""
    institucion = models.ForeignKey(Institucion, null=True)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()