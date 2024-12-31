from django import forms

from .models import InFlow


class FormInflow(forms.ModelForm):
    class Meta:
        model = InFlow
        fields = ['produto','quantidade']
        widgets = {
            'produto': forms.Select({'class' : 'form-control'}),
            'quantidade': forms.NumberInput({'class': 'form-control'})
        }