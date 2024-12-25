from django.urls import path

from .views import CreateEstoqueCarro, EstoqueCarroView

urlpatterns = [
    path('acresentar_carro/', CreateEstoqueCarro.as_view(), name='adc_carro'),
    path('lista_estoque_carro/', EstoqueCarroView.as_view(), name='lista_carro'),
]
