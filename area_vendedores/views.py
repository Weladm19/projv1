from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import VenFilipeForm
from .metrica import metrica_vendedor
from .models import VenFilipe


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