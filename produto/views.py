from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from .forms import FormProduto
from .models import Produto


# Create your views here.
class ViewProduto(ListView):
    queryset = Produto.objects.all()
    template_name = 'produtos.html'
    context_object_name = 'produtos'
    
    def get_queryset(self):
        query = super().get_queryset()
        pesquisa = self.request.GET.get('produto')
        
        if pesquisa:
            query = query.filter(produto__icontains = pesquisa)
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista De Produto'
        return context
    
class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'form-produto.html'
    form_class = FormProduto
    success_url = "/produto/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cadastro De Produto '
        return context