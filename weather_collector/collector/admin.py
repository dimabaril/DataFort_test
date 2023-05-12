from django.contrib import admin

from .models import WeatherData


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ("city", "timestamp", "temperature")
    list_filter = ("city",)
    search_fields = ("city",)
