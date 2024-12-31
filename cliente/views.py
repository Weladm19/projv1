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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'cadastrar cliente'
        return context
    
class ViewCliente(ListView):
    queryset = Cliente.objects.all()
    template_name = 'viewcliente.html'
    context_object_name = 'clientes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'cliente'
        return context