from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

class Measurement (models.Model):
    sensor_id =models.ManyToManyField(Sensor, related_name='measured')
    measuring_temperature = models.FloatField()
    date_measurement_create = models.DateTimeField(auto_now_add=True)
    date_measurement_update = models.DateTimeField(auto_now=True)
