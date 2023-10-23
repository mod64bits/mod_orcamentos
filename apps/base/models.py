from django.db import models
import uuid
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE


class Base(models.Model):
    _safedelete_policy = SOFT_DELETE
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True


class Empresa(Base):
    nome = models.CharField('Nome', max_length=150)
    cnpj = models.CharField('CNPJ', max_length=30, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=30, null=True, blank=True)
    email = models.EmailField('E-mail', null=True, blank=True)
    logo = models.ImageField('Logo', null=True, blank=True, upload_to='logos/')

    def __str__(self):
        return self.nome