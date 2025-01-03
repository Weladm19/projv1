from django import forms
from django.core.exceptions import ValidationError

from .models import OutFlow


class FormOutFlow(forms.ModelForm):
    class Meta:
        model = OutFlow
        fields = ['produto','quantidade']
        widgets = {
            'produto': forms.Select({'class' : 'form-control'}),
            'quantidade': forms.NumberInput({'class': 'form-control'})
        }
        
    def clean_quantidade(self):
        data = self.cleaned_data.get("quantidade")
        produto = self.cleaned_data.get('produto')
        
        if data > produto.quantidade:
            raise ValidationError(f'Infelizmente seu estoque possui apenas {produto.quantidade}')
        
        return data