from django.forms import ModelForm
from .models import ItemProduto, Produto
from django import forms
from faker import Faker
faker = Faker('pt_BR')

STATUS_CHOICES = (
        ("0", 'Não Enviado'),
        ("1", 'Em Analise'),
        ("2", 'Aprovado'),
        ("3", 'Cancelada'),
    )

TIPO_CALCULO_CHOICES = (
    ("0", 'Porcentagem'),
    ("1", 'Valor'),
)

class ItemProdutoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tipo_calculo"] = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS_CHOICES, initial='0')

    class Meta:
        model = ItemProduto
        fields = "__all__"


class OrcamentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"] = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS_CHOICES, initial='0')
        self.fields["total"].widget.attrs.update({'disabled': 'true'})
        self.fields["total_equipamentos"].widget.attrs.update({'disabled': 'true'})
        self.fields["total_mao_de_obra"].widget.attrs.update({'disabled': 'true'})

    class Meta:
        model = Produto
        fields = "__all__"

