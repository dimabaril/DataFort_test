from django.apps import AppConfig


class CollectorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "collector"

    def ready(self):
        # Import celery app now that Django is mostly ready.
        # This initializes Celery and autodiscovers tasks
        import weather_collector.celery
