from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
from django.db import models
from typing import Any


class CalculatorUserManager(BaseUserManager):
    def create_user(
            self,
            email: str,
            name: str,
            password: str = None,
            **extra_fields: Any
    ):
        if not email:
            raise ValueError('Usuário Obrigatório')

        user: CalculatorUser = self.model(
            name=name,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(
            self,
            email: str,
            name: str,
            password: str = None,
            **extra_fields: Any
    ):
        user: CalculatorUser = self.create_user(
            name=name,
            password=password,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)

        return user


class CalculatorUser(AbstractBaseUser):
    name = models.CharField(
        max_length=128,
        verbose_name='Nome'
    )
    email = models.EmailField(
        unique=True,
        verbose_name='E-mail'
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )
    is_admin = models.BooleanField(
        default=False,
        verbose_name='Adminitrador'
    )

    objects = CalculatorUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
