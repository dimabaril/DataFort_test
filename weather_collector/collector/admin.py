from django.contrib import admin

from .models import City, WeatherData


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ("city", "timestamp", "temperature")
    list_filter = ("city",)
    search_fields = ("city",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "population", "timestamp")
    search_fields = ("name",)
