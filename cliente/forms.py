from django import forms

from .models import Cliente


class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'acogue', 'cpf_cpnj', 'endereco', 'email', 'nivel', 'telefone']
        widgets = {
            "nome" : forms.TextInput({'class':'form-control'}),
            "acogue" : forms.TextInput({'class':'form-control'}),
            "cpf_cpnj" : forms.TextInput({'class':'form-control'}),
            "endereco" : forms.TextInput({'class':'form-control'}),
            "email" : forms.EmailInput({'class':'form-control'}),
            "nivel" : forms.Select({'class':'form-control'}),
            "telefone" : forms.TextInput({'class':'form-control'})
        }
        labels = {
                "nome" :"Nome",
                "acogue" :"Açogue",
                "cpf_cpnj" :"CPF ou CNPJ",
                "endereco" : "Endereço",
                "email" :"Email",
                "nivel" :"Status de pagador",
                "telefone" :"Telefone",
        }