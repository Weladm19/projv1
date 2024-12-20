from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Cliente)
class AdmCliente(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'nivel']
    