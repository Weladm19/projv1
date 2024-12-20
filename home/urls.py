from django.urls import path
from .views import ViewHome


urlpatterns = [
    path('', ViewHome.as_view() , name='home')
]
