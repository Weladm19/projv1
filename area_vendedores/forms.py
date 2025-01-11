from django import forms

from .models import VenFilipe, VenLoja, VenToninho


class VenFilipeForm(forms.ModelForm):
    class Meta:
        model = VenFilipe
        fields = [
            'produto','cliente','quantidade','pagamento','obs',     
        ]
        widgets = {
            "produto" : forms.Select(attrs={'class': 'form-control'}),
            "valor" : forms.NumberInput(attrs={'class': 'form-control'}),
            "cliente" : forms.Select(attrs={'class': 'form-control'}),
            "quantidade" : forms.NumberInput(attrs={'class': 'form-control'}),
            "pagamento" : forms.Select(attrs={'class': 'form-control'}),
            "obs" : forms.Textarea(attrs={'class': 'form-control' , 'rows':1}),
        }
        
    
class VenLojaForm(forms.ModelForm):
    class Meta:
        model = VenLoja
        fields = '__all__'
        widgets = {
            "produto" : forms.Select(attrs={'class': 'form-control'}),
            "valor" : forms.NumberInput(attrs={'class': 'form-control'}),
            "cliente" : forms.Select(attrs={'class': 'form-control'}),
            "quantidade" : forms.NumberInput(attrs={'class': 'form-control'}),
            "pagamento" : forms.NumberInput(attrs={'class': 'form-control'}),
            "obs" : forms.Textarea(attrs={'class': 'form-control' , 'rows': 2}),
        }
        
        
class VenToninhoForm(forms.ModelForm): 
    class Meta:
        model = VenToninho
        fields = '__all__'
        widgets = {
            "produto" : forms.Select(attrs={'class': 'form-control'}),
            "valor" : forms.NumberInput(attrs={'class': 'form-control'}),
            "cliente" : forms.Select(attrs={'class': 'form-control'}),
            "quantidade" : forms.NumberInput(attrs={'class': 'form-control'}),
            "pagamento" : forms.NumberInput(attrs={'class': 'form-control'}),
            "obs" : forms.Textarea(attrs={'class': 'form-control' , 'rows': 2}),
        }