from django.urls import path

from .views import *

urlpatterns = [
    path('produto/', ViewProduto.as_view(), name='view_prod'),
    path('cadastro_de_produto/',CreateProdutoView.as_view(), name='cad_prod'),
    path('produto/<int:pk>/detalhe/', DetailProdutoView.as_view(), name='detalhes_prod'),
    # path('produto/<int:pk>/update/',.as_view(), name=''),
    # path('produto/<int:pk>/apagar/',.as_view(), name=''),
]
