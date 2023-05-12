from django.db import models


class WeatherData(models.Model):
    """Модель для хранения данных о погоде"""

    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    dt = models.IntegerField(null=True)
    timezone = models.IntegerField(null=True)

    class Meta:
        verbose_name = "WeatherData"
        verbose_name_plural = "WeatherData"

    def __str__(self):
        return f"{self.city} - {self.timestamp} - {self.temperature}"
