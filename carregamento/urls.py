from django.urls import path

from .views import CarregamentoView

urlpatterns = [
    path('carregamento', CarregamentoView.as_view(), name='carro')
]
