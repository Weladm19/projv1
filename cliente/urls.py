from django.urls import path

from .views import CadastrarCliente, ViewCliente

urlpatterns=[
    path('cadastrarcliente/', CadastrarCliente.as_view(), name='cadastrar-cliente'),
    path('consultarcliente/', ViewCliente.as_view(), name='cliente')
]
