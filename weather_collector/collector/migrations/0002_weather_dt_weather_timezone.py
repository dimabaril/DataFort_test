# Generated by Django 4.2.1 on 2023-05-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='dt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='timezone',
            field=models.IntegerField(null=True),
        ),
    ]
