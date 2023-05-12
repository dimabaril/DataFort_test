import os

from celery import Celery

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_collector.settings")

# Создаем экземпляр приложения Celery
app = Celery("weather_collector")

# Загружаем настройки из файла settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоматическое обнаружение и регистрация задач из приложений Django
app.autodiscover_tasks()
