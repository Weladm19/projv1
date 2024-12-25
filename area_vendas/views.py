from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import FormEstoqueCarro
from .models import EstoqueCarro


# Create your views here.
class CreateEstoqueCarro(CreateView):
    model = EstoqueCarro
    form_class =FormEstoqueCarro
    template_name = 'form-estoque.html'
    success_url = '/'
    
    
class EstoqueCarroView(ListView):
    queryset = EstoqueCarro.objects.all()
    template_name = 'estoque-carro.html'
    context_object_name = 'carros'