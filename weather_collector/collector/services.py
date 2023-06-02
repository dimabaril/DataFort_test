import requests
from django.conf import settings

from loguru import logger

from collector.models import City


logger.add("services_logs_{time}.log")


def collect_cities():
    if City.objects.exists():
        logger.info("Отлуп! Города уже есть в базе данных.")
        return

    base_url = "http://api.geonames.org/"
    params = {
        "featureCode": "PPLA",
        "orderby": "population",
        "maxRows": 50,
        "username": settings.GEONAMES_USERNAME,
        "type": "json",
    }

    cities_objects = []

    try:
        response = requests.get(base_url + "search", params=params)
        response.raise_for_status()
        data = response.json()
        cities = data["geonames"]
        for city in cities:
            city = City(
                name=city["name"],
                population=city["population"],
            )
            cities_objects.append(city)

    except requests.RequestException as error:
        logger.exception(
            "Произошла ошибка при выполнении запроса:",
            error,
        )
    except (KeyError, ValueError) as error:
        logger.exception(
            "Произошла ошибка парсинга:",
            error,
        )
    except Exception as error:
        logger.exception(
            "Ой, неизвестная ошибка:",
            error,
        )

    City.objects.bulk_create(cities_objects)
