from django.contrib import admin
from .models import InforVenda

@admin.register(InforVenda)
class AdminInforVenda(admin.ModelAdmin):
    list_display = ["produto","vendedor","data_lancamento","hora_venda","total_vendido"]