from django.db import models
from apps.core.models import BaseModel


class Cliente(BaseModel):
    nome = models.CharField('Cliente/Empresa', max_length=100)
    documento = models.CharField('Documento', max_length=40, null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    endereco = models.CharField('Endereço', max_length=250, null=True, blank=True)
    observacao = models.TextField('Observação', null=True, blank=True)
    slug_from = 'nome'

    def __str__(self):
        return self.nome

