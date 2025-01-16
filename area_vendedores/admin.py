from django.contrib import admin

from .models import VenFilipe


@admin.register(VenFilipe)
class AdminFilipe(admin.ModelAdmin):
    list_display = ['produto','valor','quantidade','obs','total' ]   
    search_fields = ('produto',)
    list_filter = ('produto',)


# @admin.register(VenLoja)
# class AdminLoja(admin.ModelAdmin):
#     list_display = ['produto','valor','quantidade','obs' ]   
#     search_fields = ('produto',)
#     list_filter = ('produto',)


# @admin.register(VenToninho)
# class AdminToninho(admin.ModelAdmin):
#     list_display = ['produto','valor','quantidade','obs' ]   
#     search_fields = ('produto',)
#     list_filter = ('produto',)