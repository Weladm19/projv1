from django import forms

from .models import OutFlow


class FormOutFlow(forms.ModelForm):
    class Meta:
        model = OutFlow
        fields = ['produto','quantidade']
        widgets = {
            'produto': forms.Select({'class' : 'form-control'}),
            'quantidade': forms.NumberInput({'class': 'form-control'})
        }