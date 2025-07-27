from django.db import models
from django.conf import settings


class Operation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='operation',
        verbose_name='Usuário'
    )
    parameters = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name='Expressão'
    )
    result = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        verbose_name='Resultado'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de criação'
    )
