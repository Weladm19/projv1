from django.urls import path

from .views import home

urlpatterns = [
    path('dash/', home , name='home')
]
