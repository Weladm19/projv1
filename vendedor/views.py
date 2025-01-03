from django.views.generic import CreateView, ListView

from .forms import *
from .models import EstoqueCarroFilipe


class Teste(CreateView):
    model = EstoqueCarroFilipe
    form_class = Teste
    template_name = 'teste.html' 
    success_url = '/vendedor/filipe/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teste01"] = EstoqueCarroFilipe.objects.all()
        return context