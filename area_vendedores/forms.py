from django import forms
from django.core.exceptions import ValidationError

from .models import VenFilipe, VenToninho


class VenFilipeForm(forms.ModelForm):
    class Meta:
        model = VenFilipe
        fields = [
            'produto','quantidade','obs',     
        ]
        widgets = {
            "produto" : forms.Select(attrs={'class': 'form-control'}),
            "valor" : forms.NumberInput(attrs={'class': 'form-control'}),
            "quantidade" : forms.NumberInput(attrs={'class': 'form-control'}),
            "obs" : forms.Textarea(attrs={'class': 'form-control' , 'rows':1}),
        }
        
        
    def clean_quantidade(self):
        quanti_estoque = self.cleaned_data.get("quantidade")
        quanti_produto = self.cleaned_data.get('produto')
        
        if quanti_estoque > quanti_produto.quantidade:
            raise ValidationError(f"Seu estoque possui apenas {quanti_produto.quantidade}")
        return quanti_estoque
    
            
# class VenLojaForm(forms.ModelForm):
#     class Meta:
#         model = VenLoja
#         fields = '__all__'
#         widgets = {
#             "produto" : forms.Select(attrs={'class': 'form-control'}),
#             "valor" : forms.NumberInput(attrs={'class': 'form-control'}),
#             "quantidade" : forms.NumberInput(attrs={'class': 'form-control'}),
#             "obs" : forms.Textarea(attrs={'class': 'form-control' , 'rows': 2}),
#         }
        
#     def clean_quantidade(self):
#         quanti_estoque = self.cleaned_data.get("quantidade")
#         quanti_produto = self.cleaned_data.get('produto')
        
#         if quanti_estoque > quanti_produto.quantidade:
#             raise ValidationError(f"Seu estoque possui apenas {quanti_produto.quantidade}")
#         return quanti_estoque
        
class VenToninhoForm(forms.ModelForm): 
    class Meta:
        model = VenToninho
        fields = [
            'produto','quantidade','obs',     
        ]
        widgets = {
            "produto" : forms.Select(attrs={'class': 'form-control'}),
            "valor" : forms.NumberInput(attrs={'class': 'form-control'}),
            "quantidade" : forms.NumberInput(attrs={'class': 'form-control'}),
            "obs" : forms.Textarea(attrs={'class': 'form-control' , 'rows': 1}),
        }
    
    def clean_quantidade(self):
        quanti_estoque = self.cleaned_data.get("quantidade")
        quanti_produto = self.cleaned_data.get('produto')
        
        if quanti_estoque > quanti_produto.quantidade:
            raise ValidationError(f"Seu estoque possui apenas {quanti_produto.quantidade}")
        return quanti_estoque