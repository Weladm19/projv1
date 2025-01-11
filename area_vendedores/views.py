from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import VenFilipeForm
from .models import VenFilipe


class VenFilipeListView(CreateView):
    model = VenFilipe
    template_name = 'filipe.html'
    form_class = VenFilipeForm
    success_url = reverse_lazy('filipe_venda')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filipe_model'] = VenFilipe.objects.all()
        return context