from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('home.urls')),
    path('', include('cliente.urls')),
    path('', include('produto.urls')),
    path('', include('inflow.urls')),
    path('', include('outflow.urls')),
    path('', include('carregamento.urls')),
    path('', include('carroestoque.urls')),
]
