from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from .forms import FormCliente
from .models import Cliente


# Create your views here.
class CadastrarCliente(CreateView):
    model = Cliente
    template_name = 'cadastro.html'
    form_class = FormCliente
    success_url = "/consultarcliente/"
    
    
class ViewCliente(ListView):
    queryset = Cliente.objects.all()
    template_name = 'viewcliente.html'
    context_object_name = 'clientes'