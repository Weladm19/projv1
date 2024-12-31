from django.shortcuts import render

from .metrica import get_metricas


def home(request):
    context = {
        'metricas' : get_metricas(),
        'title' : 'Home'
    }
    return render(request, 'index.html' , context)