from django.db import models
from users.models import TimeStampedModel

# Create your models here.


class Buses(TimeStampedModel):
    class Meta:
        verbose_name = 'Autobús'
        verbose_name_plural = 'Autobuses'

    brand = models.CharField(max_length=50, verbose_name='Marca')
    model = models.CharField(max_length=50, verbose_name='Modelo')
    year = models.PositiveIntegerField(verbose_name='Año')
    capacity = models.PositiveIntegerField(default=10, verbose_name='Capacidad')
    number = models.PositiveIntegerField(default=10, verbose_name='Numero')

    def __str__(self):
        return "{} - {}".format(self.brand, self.model)
