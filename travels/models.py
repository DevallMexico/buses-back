from django.db import models
from users.models import TimeStampedModel
from drivers.models import Drivers
from bus.models import Buses

# Create your models here.


class Travels(TimeStampedModel):
    class Meta:
        verbose_name = 'Trayecto'
        verbose_name_plural = 'Trayectos'

    origin = models.CharField(max_length=50, verbose_name='Origen')
    destiny = models.CharField(max_length=50, verbose_name='Destino')
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE, related_name="travels", verbose_name='Conductor')
    bus = models.ForeignKey(Buses, on_delete=models.CASCADE, related_name="bus_travels", verbose_name='Autobus')
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.origin, self.destiny)