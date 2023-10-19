from django.contrib import admin
from .models import Marca, Categoria, Produto, Unidade


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'created')
    list_filter = ('nome', 'created')
    search_fields = ('nome', 'created',)
    list_per_page = 50
    date_hierarchy = 'created'


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'created')
    list_filter = ('nome', 'created')
    search_fields = ('nome', 'created',)
    list_per_page = 50
    date_hierarchy = 'created'

@admin.register(Unidade)
class SigraAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'descricao', 'created')
    list_filter = ('sigla', 'created')
    search_fields = ('sigla', 'created',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'categoria', 'marca', 'unidade')
    list_filter = ('codigo', 'marca')
    search_fields = ('codigo', 'descricao', 'created',)
    list_per_page = 50
    date_hierarchy = 'created'

    fieldsets = [
        (
            None,
            {
                "fields": ["descricao", "categoria", "marca", "unidade", "inf_adicionais"],
            },

        ),
        (
            "Valor de Compra",
            {
                "fields": ["custo"],
            },
        ),
    ]
