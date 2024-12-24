from django.contrib import admin

from inflow.models import InFlow


# Register your models here.
@admin.register(InFlow)
class AdmInFlow(admin.ModelAdmin):
    ...