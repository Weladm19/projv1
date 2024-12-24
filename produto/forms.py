from django import forms

from .models import Produto


class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['produto','tipo','marca','custo','preco_venda','quantidade']
        widgets = {
            'produto': forms.TextInput({'class': 'form-control'}),
            'tipo': forms.Select({'class': 'form-control'}),
            'marca': forms.TextInput({'class': 'form-control'}),
            'custo': forms.NumberInput({'class': 'form-control'}),
            'preco_venda': forms.NumberInput({'class': 'form-control'}),
            'quantidade': forms.NumberInput({'class': 'form-control'}),
        }
        labels = {
            'produto': 'Nome Do Produto',
            'tipo': 'Tipo Do Produto',
            'marca': 'Marca',
            'custo': 'Custo De Compra',
            'preco_venda': 'Custo de Venda',
            'quantidade': 'Quantidade',
        }