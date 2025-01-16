from django.urls import path

from .views import (CarroFilipeFormView, CarroToninhoFormView,
                    DeleteCarEstoqueFilipe, DeleteCarEstoqueToninho,
                    EstoqueCarroFilipeView, EstoqueCarroToninhoView)

urlpatterns = [
    path('carro_filipe/', CarroFilipeFormView.as_view() ,name='carro_filipe'),
    path('carro_toninho/', CarroToninhoFormView.as_view() ,name='carro_toninho'),
    path('estoque_filipe/', EstoqueCarroFilipeView.as_view() ,name='estoque_filipe'),
    path('estoque_toninho/', EstoqueCarroToninhoView.as_view() ,name='estoque_toninho'),
    path('estoque_filipe/delete/<int:pk>/', DeleteCarEstoqueFilipe.as_view() ,name='delete_carro_filipe'),
    path('estoque_toninho/delete/<int:pk>/', DeleteCarEstoqueToninho.as_view() ,name='delete_carro_toninho'),
]
