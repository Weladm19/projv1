from django.contrib import admin

from .models import InFlow, OutFlow


# Register your models here.
# Register your models here.
@admin.register(InFlow)
class AdmInflow(admin.ModelAdmin):
    list_display = ["tipo_in"]
    
@admin.register(OutFlow)
class AdmOutFlow(admin.ModelAdmin):
    list_display = ["tipo_ou"]
    