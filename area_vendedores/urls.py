from django.urls import path

from .views import (VenFilipeDeleteView, VenFilipeEstoqueView,
                    VenFilipeListView, VenFilipeUpdateView)

urlpatterns = [
    path('vendas_filipe/' , VenFilipeListView.as_view() , name='filipe_venda'),
    path("estoque_carro_filipe/", VenFilipeEstoqueView.as_view(), name="estoque_f"),
    path('vendas_filipe/update/<int:pk>/', VenFilipeUpdateView.as_view(), name='alter_preço_filipe'),
    path('vendas_filipe/delete/<int:pk>/', VenFilipeDeleteView.as_view(), name='delete_produto'),
]