from django import forms

from .models import EstoqueCarro


class FormEstoqueCarro(forms.ModelForm):
    class Meta:
        model = EstoqueCarro
        fields = ['vendedor','produto','quantidade','valor_material']