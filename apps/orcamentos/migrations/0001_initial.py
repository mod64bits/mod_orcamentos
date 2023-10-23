# Generated by Django 4.1 on 2023-10-19 16:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('produtos', '0001_initial'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('validade', models.DateField(default=datetime.date(2023, 11, 3), verbose_name='Validade')),
                ('codigo', models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True, verbose_name='Codigo')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
                ('total_equipamentos', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Equipamentos')),
                ('total_mao_de_obra', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Mão de Obra')),
                ('total_lucro', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Lucro')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orcamento_cliente', to='clientes.clientes', verbose_name='Cliente')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_orcamento', to='base.empresa', verbose_name='Empresa para o Orçamento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('calculo_produtos', models.CharField(default=0, max_length=2, verbose_name='Forma de Calculo')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Preço')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produto_orcamento', to='orcamentos.orcamento', verbose_name='Orcamento')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_produto', to='produtos.produto', verbose_name='Produto')),
            ],
        ),
    ]