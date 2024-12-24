from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import FormInflow
from .models import InFlow


# Create your views here.
class FormInFlowView(CreateView):
    model = InFlow
    template_name = 'in.html'
    form_class = FormInflow
    success_url= reverse_lazy('entrada')
    

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Entrada em estoque'
            return context
        
        
class InflowView(ListView):
    queryset = InFlow.objects.all()
    template_name = 'entradas.html'
    context_object_name = 'inflows'