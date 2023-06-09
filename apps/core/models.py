from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True
