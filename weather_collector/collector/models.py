from django.db import models


class City(models.Model):
    """Модель для хранения городов"""

    name = models.CharField(max_length=100)
    population = models.IntegerField()
    # timezone = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-population"]
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class WeatherData(models.Model):
    """Модель для хранения данных о погоде"""

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    dt = models.IntegerField(null=True)
    timezone = models.IntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "WeatherData"
        verbose_name_plural = "WeatherData"

    def __str__(self):
        return f"{self.city} - {self.timestamp} - {self.temperature}"
