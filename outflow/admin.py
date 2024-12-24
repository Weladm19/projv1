from django.contrib import admin


# Register your models here.
class AdmOutFlow(admin.ModelAdmin):
    list_display = ['produto']