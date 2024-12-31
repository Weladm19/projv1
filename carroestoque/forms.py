from django import forms

from .models import EstoqueCarroFilipe, EstoqueCarroToninho


class FilipeForm(forms.ModelForm):
    class Meta:
        model = EstoqueCarroFilipe
        fields = '__all__'
        
    
class ToninhoForm(forms.ModelForm):
    class Meta:
        model = EstoqueCarroToninho
        fields = '__all__'