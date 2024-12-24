from django.urls import path

from .views import *

urlpatterns = [
    path('produto/', ViewProduto.as_view(), name='view_prod'),
    path('cadastro_de_produto/',CreateProdutoView.as_view(), name='cad_prod')
]
