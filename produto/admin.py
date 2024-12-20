from django.contrib import admin

from .models import Produto, Tipo


# Register your models here.
@admin.register(Produto)
class AdmProduto(admin.ModelAdmin):
    list_display = ["produto","tipo","marca","custo","preco_venda","quantidade"]
    
    
# Register your models here.
@admin.register(Tipo)
class AdmTipo(admin.ModelAdmin):
    list_display = ["tipo"]