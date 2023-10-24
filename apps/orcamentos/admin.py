from django.contrib import admin
from .models import ItemProduto, Orcamento
from .forms import OrcamentoForm, ItemProdutoForm
from django_summernote.admin import SummernoteModelAdmin


class ItemProdutoInline(admin.TabularInline):
    model = ItemProduto
    extra = 0

    def save(self, request, obj, form, change):
        if obj.tipo_calculo == "1":
            obj.save()


@admin.register(ItemProduto)
class ItemProdutoAdmin(admin.ModelAdmin):
    form = ItemProdutoForm
    list_display = ("orcamento", "produto", "quantidade", "preco", "total")

    list_per_page = 50
    date_hierarchy = 'created'

    fieldsets = [
        (
            "Orçamento",
            {
                "fields": ["orcamento"]
            },
        ),
        (
            "Produto",
            {
                "fields": [("produto", "quantidade")],
                "classes": ["collapse"]
            },
        ),

        (
            "Tipo de Calculo",
            {
                "fields": ["tipo_calculo"]
            },

        ),
        (
            "Valores",
            {
                "fields": ["preco", "total"]
            },
        ),
    ]


@admin.register(Orcamento)
class OrcamentoAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    form = OrcamentoForm
    radio_fields = {"status": admin.VERTICAL}
    list_display = ("codigo", "titulo", "cliente", "validade", "total_equipamentos", "total", "status")
    list_editable = ["status"]
    inlines = [
        ItemProdutoInline,
    ]

    fieldsets = [
        (
            "Titulo",
            {
                "fields": ["titulo"]
            },
        ),
        (
            "Lucro",
            {
                "fields": ["total_lucro"]
            },
        ),
        (
            "Orçamento",
            {
                "fields": [("cliente", "empresa", "validade", "status"), "descricao",
                           ("total_equipamentos", "total_mao_de_obra", "total")],
            },
        ),
    ]

    class Media:
        js = ('orcamento/js/item_ptoduto.js',)