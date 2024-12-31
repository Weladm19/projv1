from django.urls import path

from .views import (CarroFilipeFormView, CarroToninhoFormView,
                    EstoqueCarroFilipeView, EstoqueCarroToninhoView)

urlpatterns = [
    path('carro_filipe/', CarroFilipeFormView.as_view() ,name='carro_filipe'),
    path('carro_toninho/', CarroToninhoFormView.as_view() ,name='carro_toninho'),
    path('estoque_filipe/', EstoqueCarroFilipeView.as_view() ,name='estoque_filipe'),
    path('estoque_toninho/', EstoqueCarroToninhoView.as_view() ,name='estoque_toninho'),
]
