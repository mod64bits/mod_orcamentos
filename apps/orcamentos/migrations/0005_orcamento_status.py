# Generated by Django 4.1 on 2023-10-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orcamentos', '0004_itemproduto_created_itemproduto_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orcamento',
            name='status',
            field=models.CharField(choices=[(0, 'Não Enviado'), (1, 'Em Analise'), (2, 'Aprovado'), (3, 'Cancelada')], default=0, max_length=1, verbose_name='Status'),
        ),
    ]
