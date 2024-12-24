from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from outflow.forms import FormOutFlow
from outflow.models import OutFlow


# Create your views here.
class OutFlowView(ListView):
    queryset = OutFlow.objects.all()
    template_name='saidas.html'
    context_object_name = 'outflows'
    

class FormOutFlowView(CreateView):
    model = OutFlow
    form_class = FormOutFlow
    template_name = 'out.html'
    success_url = reverse_lazy('saida')
    