# Generated by Django 4.2.1 on 2023-05-12 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0003_alter_weather_dt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weather',
            new_name='WeatherData',
        ),
    ]