from django import forms
from django.core.exceptions import ValidationError

from .models import EstoqueCarroFilipe, EstoqueCarroToninho


class FilipeForm(forms.ModelForm):
    class Meta:
        model = EstoqueCarroFilipe
        fields = ['produto','quantidade']
        
    def clean_quantidade(self):
        data = self.cleaned_data.get("quantidade")
        produto = self.cleaned_data.get('produto')
        
        if data > produto.quantidade:
            raise ValidationError(f'Infelizmente seu estoque possui apenas {produto.quantidade}')
        
        return data
    
    
class ToninhoForm(forms.ModelForm):
    class Meta:
        model = EstoqueCarroToninho
        fields = ['produto','quantidade']
        
    def clean_quantidade(self):
        data = self.cleaned_data.get("quantidade")
        produto = self.cleaned_data.get('produto')
        
        if data > produto.quantidade:
            raise ValidationError(f'Infelizmente seu estoque possui apenas {produto.quantidade}')
        
        return data