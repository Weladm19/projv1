from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView

from carroestoque.metrica import get_metricas_filipe, get_metricas_toninho

from .forms import FilipeForm, ToninhoForm
from .models import EstoqueCarroFilipe, EstoqueCarroToninho


# Create your views here.
class CarroFilipeFormView(CreateView):
    model = EstoqueCarroFilipe
    form_class = FilipeForm
    template_name= 'in-carro.html'
    success_url = '/carro_filipe/'
    

class CarroToninhoFormView(CreateView):
    model = EstoqueCarroToninho
    form_class = ToninhoForm
    template_name= 'in-carro.html'
    success_url = '/carro_toninho/'
    
    
class EstoqueCarroFilipeView(ListView):
    queryset = EstoqueCarroFilipe.objects.all()
    template_name = 'estoque_carro_filipe.html'
    context_object_name = 'car_filipe'

    def get_queryset(self):
        query_filipe = super().get_queryset()
        search_filipe = self.request.GET.get('carro_filipe')
        if search_filipe:
            query_filipe = query_filipe.filter(produto__produto__icontains=search_filipe)
        return query_filipe
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estoque filipe'
        context['custo'] = get_metricas_filipe()
        
        return context


class EstoqueCarroToninhoView(ListView):
    queryset = EstoqueCarroToninho.objects.all()
    template_name = 'estoque_carro_toninho.html'
    context_object_name = 'car_toninho'

    def get_queryset(self):
        query_toninho = super().get_queryset()
        search_toninho = self.request.GET.get('carro_toninho')
        if search_toninho:
            query_toninho = query_toninho.filter(produto__produto__icontains = search_toninho)
        return query_toninho
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Estoque toninho'
        context['custo'] = get_metricas_toninho()
        return context
    

class DeleteCarEstoqueFilipe(DeleteView):
    model = EstoqueCarroFilipe
    template_name = 'delete_estoque_carro_filipe.html'
    success_url = reverse_lazy('estoque_filipe')
    
    
class DeleteCarEstoqueToninho(DeleteView):
    model = EstoqueCarroToninho
    template_name = 'delete_estoque_carro_filipe.html'
    success_url = reverse_lazy('estoque_toninho')
    