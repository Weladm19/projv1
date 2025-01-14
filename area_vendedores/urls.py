from django.urls import path

from .views import VenFilipeDeleteView, VenFilipeListView, VenFilipeUpdateView

urlpatterns = [
    path('vendas_filipe/' , VenFilipeListView.as_view() , name='filipe_venda'),
    path('vendas_filipe/update/<int:pk>/', VenFilipeUpdateView.as_view(), name='alter_preço_filipe'),
    path('vendas_filipe/delete/<int:pk>/', VenFilipeDeleteView.as_view(), name='delete_produto'),
]
