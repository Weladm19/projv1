from django.apps import AppConfig


class CarroestoqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carroestoque'


    def ready(self):
        import carroestoque.signals