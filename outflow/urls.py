from django.urls import path

from .views import FormOutFlowView, OutFlowView

urlpatterns = [
    path('saida/',FormOutFlowView.as_view(), name='saida'),
    path('saida/lista/', OutFlowView.as_view(), name='saida_view')
]
