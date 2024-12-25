from django.contrib import admin

from .models import EstoqueCarro


# Register your models here.
@admin.register(EstoqueCarro)
class AdmEstoqueCarro(admin.ModelAdmin):
    list_display = ['vendedor','produto','quantidade','valor_material','data_de_adicao']