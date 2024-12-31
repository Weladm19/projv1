from django.views.generic import CreateView, ListView

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
        context['title'] = 'estoque filipe'
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
        context['title'] = 'estoque toninho'
        return context