# Generated by Django 4.0.4 on 2022-05-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.IntegerField()),
                ('measuring_temperature', models.FloatField()),
                ('date_measurement_create', models.DateTimeField(auto_now_add=True)),
                ('date_measurement_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
            ],
        ),
    ]
