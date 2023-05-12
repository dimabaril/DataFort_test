import requests

from .models import WeatherData

API_KEY = "cc4a59be6e427ede277ae4d9ee4acde4"

# тут силы закончились и появился список )
CITIES = [
    "Tokyo",
    "Delhi",
    "Shanghai",
    "São Paulo",
    "Mumbai",
    "Beijing",
    "Cairo",
    "Dhaka",
    "Mexico City",
    "Osaka",
    "Karachi",
    "Chongqing",
    "Istanbul",
    "Buenos Aires",
    "Kolkata",
    "Lagos",
    "Kinshasa",
    "Manila",
    "Rio de Janeiro",
    "Guangzhou",
    "Shenzhen",
    "Lahore",
    "Bangalore",
    "Moscow",
    "Jakarta",
    "London",
    "Lima",
    "Bangkok",
    "Chennai",
    "New York City",
    "Chengdu",
    "Nairobi",
    "Hong Kong",
    "Ho Chi Minh City",
    "Hangzhou",
    "Rio de Janeiro",
    "Wuhan",
    "Tianjin",
    "Ahmedabad",
    "Kuala Lumpur",
    "Riyadh",
    "Los Angeles",
    "Baghdad",
    "Santiago",
    "Hyderabad",
    "Boston",
    "Dallas",
    "Chicago",
    "Toronto",
    "Miami",
]


def collect_weather_data():
    print("collector!!!!!     Collecting weather data!!!!!!!!!!")

    weather_objects = []

    for city in CITIES:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        )

        data = requests.get(url).json()

        # city = data["name"]
        # temperature = data["main"]["temp"]
        # humidity = data["main"]["humidity"]
        # wind_speed = data["wind"]["speed"]
        # dt = data["dt"]
        # timezone = data["timezone"]

        weather = WeatherData(
            city=data["name"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            dt=data["dt"],
            timezone=data["timezone"],
        )
        # weather.save()
        weather_objects.append(weather)

    WeatherData.objects.bulk_create(weather_objects)
