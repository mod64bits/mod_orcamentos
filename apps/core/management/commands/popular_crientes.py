import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.clientes.models import Clientes
faker = Faker('pt_BR')


def add_clientes(qt):
    for _ in range(0, qt):
        Clientes.objects.create(
            documento=faker.cnpj(),
            whatsApp=faker.phone_number()
        )


class Command(BaseCommand):
    help = "popular cliente"

    def handle(self, *args, **options):
        add_clientes(500)