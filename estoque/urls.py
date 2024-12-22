from django.urls import path

from .views import cadOutFlow

urlpatterns=[
    path('saida/', cadOutFlow.as_view(),name='saida')
]
