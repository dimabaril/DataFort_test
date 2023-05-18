from celery import shared_task
from loguru import logger

from .collector import collect_weather_data


logger.add("tasks_logs_{time}.log")


@shared_task
def collect_weather_periodically():
    logger.info("Таска collect_weather_periodically пошла.")
    collect_weather_data()
