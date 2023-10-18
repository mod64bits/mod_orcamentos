from django.db import models
from apps.base.models import Base
from apps.clientes.models import Clientes

TIPO_ENDERECO = [
    ('UNI', 'Único'),
    ('RES', 'Residencial'),
    ('COM', 'Comercial'),
    ('COB', 'Cobrança'),
    ('ENT', 'Entrega'),
    ('OUT', 'Outro'),
]

UF_SIGLA = [
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('EX', 'EX'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
]


class Enderecos(Base):
    cliente_end = models.ForeignKey(
        Clientes,
        verbose_name="Cliente",
        related_name="endereco",
        on_delete=models.CASCADE
    )
    tipo_endereco = models.CharField("Tipo", max_length=3, null=True, blank=True, choices=TIPO_ENDERECO)
    logradouro = models.CharField("Logradouro", max_length=255, null=True, blank=True)
    numero = models.CharField("Numero", max_length=16, null=True, blank=True)
    bairro = models.CharField("Bairro", max_length=64, null=True, blank=True)
    complemento = models.CharField("complemento", max_length=64, null=True, blank=True)
    municipio = models.CharField("Municipio", max_length=64, null=True, blank=True)
    cep = models.CharField("CEP", max_length=16, null=True, blank=True)
    uf = models.CharField("UF", max_length=3, null=True,
                          blank=True, choices=UF_SIGLA, default='SP')

    @property
    def format_endereco(self):
        return '{0}, {1} - {2}'.format(self.logradouro, self.numero, self.bairro)

    @property
    def format_endereco_completo(self):
        return '{0} - {1} - {2} - {3} - {4} - {5}'.format(self.logradouro, self.numero, self.bairro,
                                                          self.municipio, self.cep, self.uf)

    def __str__(self):
        s = u'%s, %s, %s (%s)' % (
            self.logradouro, self.numero, self.municipio, self.uf)
        return s