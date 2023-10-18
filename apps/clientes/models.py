from django.db import models
from apps.base.models import Base
from apps.accounts.models import User


class Clientes(Base):
    TIPO_CLIENTE = [
        ('normal', 'Normal'),
        ('contrato', 'Contrato'),
    ]
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='client_user',
        null=True,
        blank=True
    )
    documento = models.CharField('Documento', max_length=50, null=True, blank=True)
    whatsApp = models.CharField('WhatsApp', max_length=50)
    tipo_cliente = models.CharField(
        max_length=30, choices=TIPO_CLIENTE, default='normal')
    bloqueado = models.BooleanField('Bloqueado', default=False)

    def __str__(self):
        return self.whatsApp
