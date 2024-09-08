# myapp3/apps.py

from django.apps import AppConfig

class Myapp3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp3'

    def ready(self):
        import myapp3.signals
