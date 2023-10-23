import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.produtos.models import Categoria, Unidade, Marca, Produto
faker = Faker()


def criar_categoria(qt):
    sigra = ["UN", "MT", "KG"]
    for _ in range(1, qt):
        description = None
        _si = random.choice(sigra)
        if _si == "UN":
            description = "Unidade"
        elif _si == "MT":
            description = "Metro"
        elif _si == "KG":
            description = "Kilo grama"
        cat = Categoria.objects.create(nome=faker.user_name())
        marc = Marca.objects.create(nome=faker.user_name())
        unid = Unidade.objects.create(sigla=_si, descricao=description)

        Produto.objects.create(
            codigo=faker.nic_handle(),
            descricao=faker.currency_name(),
            categoria=cat,
            marca=marc,
            unidade=unid,
            inf_adicionais=faker.catch_phrase(),
            custo=10
        )


class Command(BaseCommand):
    help = "Pupulation Product"

    def handle(self, *args, **options):
        criar_categoria(500)