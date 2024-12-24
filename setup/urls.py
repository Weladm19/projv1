from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('cliente.urls')),
    path('', include('produto.urls')),
    path('', include('inflow.urls')),
    path('', include('outflow.urls')),
]
