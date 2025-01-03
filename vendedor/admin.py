from django.contrib import admin

from .models import VenderFilipe


# Register your models here.
@admin.register(VenderFilipe)
class AdmVendedor(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'valor_cliente', 'pagamento']