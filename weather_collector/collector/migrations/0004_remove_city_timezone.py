# Generated by Django 4.2 on 2023-06-02 01:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("collector", "0003_alter_city_options_alter_city_population"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="city",
            name="timezone",
        ),
    ]