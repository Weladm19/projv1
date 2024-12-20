from django.urls import path

from .views import *

urlpatterns = [
    path('cadastro_de_produto/', ViewProduto.as_view(), name='view_prod')
]
