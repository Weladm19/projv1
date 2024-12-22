from django import forms

from .models import InFlow, OutFlow


class FormInflow(forms.ModelForm):
    class Meta:
        model = InFlow
        fields = ['tipo_in', 'quantidade_pro']

class FormOutFlow(forms.ModelForm):
    class Meta:
        model = OutFlow
        fields = ['tipo_ou', 'quantidade_pro']
