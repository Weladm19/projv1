from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

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
        context['title'] = 'lista de produto'
        return context
    
class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'form-produto.html'
    form_class = FormProduto
    success_url = "/produto/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'cadastro de produto '
        return context
    
    
class DetailProdutoView(DetailView):
    model = Produto
    template_name = 'detalhe-produto.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'detalhe'
        return context
    
    
class UpdateProdutoView(UpdateView):
    model = Produto
    form_class = FormProduto
    template_name = 'update-produto.html'
    success_url = reverse_lazy('view_prod')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'update'
        return context

class ApagarProdutoView(DeleteView):
    ...