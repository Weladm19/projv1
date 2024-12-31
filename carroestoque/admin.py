from django.contrib import admin

from .models import EstoqueCarroFilipe, EstoqueCarroToninho


# Register your models here.
@admin.register(EstoqueCarroFilipe)
class AdmFelipe(admin.ModelAdmin):
    list_display = ['produto','quantidade','data_entrada']
    
    
# Register your models toninho.
@admin.register(EstoqueCarroToninho)
class AdmToninho(admin.ModelAdmin):
    list_display = ['produto','quantidade','data_entrada']