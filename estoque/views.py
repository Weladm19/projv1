from django.shortcuts import redirect
from django.views.generic import FormView

from estoque.forms import FormInflow, FormOutFlow
from estoque.models import InFlow, OutFlow


# Create your views here.
class cadOutFlow(FormView):
    model = OutFlow
    form_class = FormOutFlow
    template_name = 'out.html'
    success_url = '/saida/'