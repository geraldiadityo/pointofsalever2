from django.apps import AppConfig


class PenggunaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pengguna'

    def ready(self):
        import pengguna.signals
