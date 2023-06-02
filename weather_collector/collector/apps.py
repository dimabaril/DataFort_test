from django.apps import AppConfig


class CollectorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "collector"

    def ready(self):
        import weather_collector.celery
