from django.urls import path

from .views import VenFilipeListView

urlpatterns = [
    path('vendas_filipe/' , VenFilipeListView.as_view() , name='filipe_venda'),
]
