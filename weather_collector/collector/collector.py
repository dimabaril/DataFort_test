import requests
from django.conf import settings

from loguru import logger

from collector.models import City, WeatherData

logger.add("collector_logs_{time}.log")


CITIES = City.objects.all()


def collect_weather_data():
    logger.info("Функция сбора данных о погоде collect_weather_data запущена.")

    weather_objects = []

    for city in CITIES:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid={settings.OPENWEAWERMAP_API_KEY}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            weather = WeatherData(
                city=city,
                temperature=data["main"]["temp"],
                humidity=data["main"]["humidity"],
                wind_speed=data["wind"]["speed"],
                dt=data["dt"],
                timezone=data["timezone"],
            )
            weather_objects.append(weather)

        except requests.RequestException as error:
            logger.exception(
                f"Произошла ошибка при выполнении запроса для города {city}:",
                error,
            )
        except (KeyError, ValueError) as error:
            logger.exception(
                f"Произошла ошибка парсинга для города {city}:",
                error,
            )
        except Exception as error:
            logger.exception(
                f"Ой, неизвестная ошибка для города {city}:",
                error,
            )

    WeatherData.objects.bulk_create(weather_objects)
