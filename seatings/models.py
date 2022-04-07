from django.db import models
from users.models import TimeStampedModel
from travels.models import Travels
from drivers.models import PersonalInformation

# Create your models here.


class Seatings(TimeStampedModel, PersonalInformation):
    class Meta:
        verbose_name = 'Asiento'
        verbose_name_plural = 'Asientos'

    travel = models.ForeignKey(Travels, on_delete=models.CASCADE, related_name="seatings", verbose_name='Trayecto')
    seat_number = models.PositiveIntegerField(default=10, verbose_name='Número de asiento')

    def __str__(self):
        return "{} - {}".format(self.travel, self.seat_number)
