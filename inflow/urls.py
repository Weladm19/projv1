from django.urls import path

from .views import FormInFlowView, InflowView

urlpatterns = [
    path('entrada/',FormInFlowView.as_view(), name='entrada'),
    path('entrada/lista/', InflowView.as_view(), name='inflow_view')
]
