from django.db import models
from apps.base.models import Base
from django.core.validators import MinValueValidator
from decimal import Decimal


class Categoria(Base):
    nome = models.CharField("Nome", max_length=32)

    def __str__(self):
        return self.nome


class Marca(Base):
    nome = models.CharField("Nome", max_length=32)

    def __str__(self):
        return self.nome


class Unidade(Base):
    sigla = models.CharField("Sigla", max_length=3)
    descricao = models.CharField("Descrição", max_length=16)

    class Meta:
        verbose_name = "Unidade"

    def __str__(self):
        return f"{self.sigla}--{self.descricao}"


class Produto(Base):
    codigo = models.CharField("Código", max_length=50, null=True, blank=True, editable=False, unique=True)
    descricao = models.CharField("Descrição",   max_length=255)
    categoria = models.ForeignKey(
        Categoria,
        verbose_name="Categoria",
        related_name="categoria_produto",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    marca = models.ForeignKey(
        Marca,
        verbose_name="Marca",
        related_name="marca_produto",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    unidade = models.ForeignKey(
        Unidade,
        verbose_name="Unidade",
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    custo = models.DecimalField(max_digits=16, decimal_places=2, validators=[
        MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    inf_adicionais = models.CharField("Informações Adicionais", max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Código: {self.codigo}-Descrição: {self.descricao}-Custo: {self.custo}"
