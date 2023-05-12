from celery import shared_task

from .collector import collect_weather_data


@shared_task
def collect_weather_periodically():
    # print("tasks!!!!!     Collect_weather_periodically!!!!!!!!!!")
    collect_weather_data()
