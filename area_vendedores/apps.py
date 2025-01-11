from django.apps import AppConfig


class AreaVendedoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'area_vendedores'

    def ready(self):
        import area_vendedores.signals