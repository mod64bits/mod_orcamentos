from django.forms import ModelForm
from .models import ItemProduto, Produto
from django import forms
from datetime import date
from faker import Faker
fake = Faker()

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

    class Meta:
        model = Produto
        fields = "__all__"

    def save(self, commit=True):
        obj = super(OrcamentoForm, self).save(commit=False)
        obj.codigo = fake.bothify(text=F"", letters='ABCDE')
        if commit:
            obj.save()
        return obj