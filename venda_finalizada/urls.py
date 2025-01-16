from django.urls import path
from .views import teste

urlpatterns = [
    path('teste/', teste.as_view(),name='teste')
]
