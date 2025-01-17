from django.urls import path

from .views import (VenFilipeDeleteView, VenFilipeListView,
                    VenFilipeUpdateView, VenToninhoDeleteView,
                    VenToninhoListView, VenToninhoUpdateView)

urlpatterns = [
    path('vendas_filipe/' , VenFilipeListView.as_view() , name='filipe_venda'),
    path('vendas_filipe/update/<int:pk>/', VenFilipeUpdateView.as_view(), name='alter_preço_filipe'),
    path('vendas_filipe/delete/<int:pk>/', VenFilipeDeleteView.as_view(), name='delete_produto'),
    path('vendas_toninho/' , VenToninhoListView.as_view() , name='toninho_venda'),
    path('vendas_toninho/update/<int:pk>/', VenToninhoUpdateView.as_view(), name='alter_preço_toninho'),
    path('vendas_toninho/delete/<int:pk>/', VenToninhoDeleteView.as_view(), name='delete_produto_toninho'),
]