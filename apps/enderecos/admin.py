from django.contrib import admin
from .models import Enderecos


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cliente_end', 'tipo_endereco', 'logradouro', 'numero', 'bairro', 'municipio', 'cep')
    list_filter = ('municipio', 'created',)
    search_fields = ('cliente_end', 'municipio',)
    list_per_page = 50
    date_hierarchy = 'created'

    fieldsets = [
        (
            "Cliente Cadastrado",
            {
                "fields": ["cliente_end"],
                "description": "Selecione ou cadastre um cliente"
            },
        ),
        (
            None,
            {
                "fields": ["cep", "tipo_endereco", "logradouro", "numero", "bairro", "municipio", "uf"],
            }
        ),
    ]


admin.site.register(Enderecos, EnderecoAdmin)
