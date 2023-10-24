from django.db import models
from apps.base.models import Base, Empresa
from apps.clientes.models import Clientes
from apps.produtos.models import Produto
from apps.core.ultils import Datas


class Orcamento(Base):
    STATUS_CHOICES = (
        ("0", 'Não Enviado'),
        ("1", 'Em Analise'),
        ("2", 'Aprovado'),
        ("3", 'Cancelada'),
    )
    titulo = models.CharField("Titulo", max_length=255)
    status = models.CharField("Status", max_length=1, choices=STATUS_CHOICES, default="0")
    validade = models.DateField('Validade', default=Datas().vencimento())
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        verbose_name='Empresa',
        related_name='empresa_orcamento',
    )
    codigo = models.CharField("Codigo", max_length=20, editable=False,  unique=True, null=True, blank=True)
    cliente = models.ForeignKey(
        Clientes,
        on_delete=models.CASCADE,
        verbose_name='Cliente',
        related_name='orcamento_cliente'
    )
    descricao = models.TextField('Descrição')
    total = models.DecimalField('Total', decimal_places=2, max_digits=8, null=True, blank=True)
    total_equipamentos = models.DecimalField('Total Equipamentos', decimal_places=2, max_digits=8, null=True,
                                             blank=True)
    total_mao_de_obra = models.DecimalField('Total Mão de Obra', decimal_places=2, max_digits=8, null=True, blank=True)
    total_lucro = models.DecimalField('Total Lucro', decimal_places=2, max_digits=8, null=True, blank=True)

    def __str__(self):
        return self.titulo


class ItemProduto(Base):
    TIPO_CALCULO_CHOICES = (
        ("0", "Valor"),
        ("1", "Porcentagem")
    )

    orcamento = models.ForeignKey(
        Orcamento,
        on_delete=models.CASCADE,
        verbose_name='Orcamento',
        related_name='produto_orcamento'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        verbose_name='Produto',
        related_name='item_produto',
    )
    quantidade = models.PositiveIntegerField('Quantidade', default=1)

    tipo_calculo = models.CharField("Tipo de Calculo", max_length=2, choices=TIPO_CALCULO_CHOICES, default="1")

    valor_porcentagem = models.DecimalField('Porcentagem', decimal_places=2, max_digits=8, null=True, blank=True)
    valor_acrescimo = models.DecimalField('Acréscimo', decimal_places=2, max_digits=8, null=True, blank=True)
    lucro_venda = models.DecimalField("Lucro venda", decimal_places=2, max_digits=8, null=True, blank=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8, null=True, blank=True)
    total = models.DecimalField('Total', decimal_places=2, max_digits=8, null=True, blank=True)

    def __str__(self):
        return self.produto.codigo

