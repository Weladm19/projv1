from django.urls import path

from .views import Teste

urlpatterns = [
    path('vendedor/filipe/', Teste.as_view(), name='vendedor_f'),
]
