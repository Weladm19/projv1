from django.contrib import admin

from .models import Vendedor


# Register your models here.
@admin.register(Vendedor)
class AdmVendedor(admin.ModelAdmin):
    list_display = ['nome']