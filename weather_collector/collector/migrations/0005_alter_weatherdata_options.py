# Generated by Django 4.2.1 on 2023-05-12 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0004_rename_weather_weatherdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weatherdata',
            options={'verbose_name': 'WeatherData', 'verbose_name_plural': 'WeatherData'},
        ),
    ]
