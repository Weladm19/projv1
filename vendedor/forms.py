from django import forms

from .models import VenderFilipe


class Teste(forms.ModelForm):
    class Meta:
        model = VenderFilipe
        fields = '__all__'