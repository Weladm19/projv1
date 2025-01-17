from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import VenFilipeForm, VenToninhoForm
from .metrica import metrica_vendedor, metrica_vendedor_toninho
from .models import VenFilipe, VenToninho

# from carroestoque.models import EstoqueCarroFilipe, EstoqueCarroToninho

class VenFilipeListView(CreateView):
    model = VenFilipe
    template_name = 'filipe.html'
    form_class = VenFilipeForm
    success_url = reverse_lazy('filipe_venda')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filipe_model'] = VenFilipe.objects.all()
        context['valorfinal'] = metrica_vendedor()
        return context   
    
        
class VenFilipeUpdateView(UpdateView):
    model = VenFilipe
    template_name = 'update.html'
    fields = ['valor']
    success_url = reverse_lazy('filipe_venda')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filipe_model'] = VenFilipe.objects.all()
        context['title'] = 'Altera Valor'
        return context
    
    
class VenFilipeDeleteView(DeleteView):
    model = VenFilipe
    template_name = 'delete.html'
    success_url = reverse_lazy('filipe_venda')
    
    
# Toninho   
class VenToninhoListView(CreateView):
    model = VenToninho
    template_name = 'toninho.html'
    form_class = VenToninhoForm
    success_url = reverse_lazy('toninho_venda')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['toninho_model'] = VenToninho.objects.all()
        context['valorfinal'] = metrica_vendedor_toninho()
        return context   
    
        
class VenToninhoUpdateView(UpdateView):
    model = VenToninho
    template_name = 'update.html'
    fields = ['valor']
    success_url = reverse_lazy('toninho_venda')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['toninho_model'] = VenToninho.objects.all()
        context['title'] = 'Altera Valor'
        return context
    
    
class VenToninhoDeleteView(DeleteView):
    model = VenToninho
    template_name = 'delete.html'
    success_url = reverse_lazy('toninho_venda')