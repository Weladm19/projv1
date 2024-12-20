from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Produto


# Create your views here.
class ViewProduto(ListView):
    queryset = Produto.objects.all()
    template_name = 'produtos.html'
    context_object_name = 'produtos'