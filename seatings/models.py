from django.db import models
from users.models import TimeStampedModel
from travels.models import TravelsSchedule
from drivers.models import PersonalInformation

# Create your models here.


class Seatings(TimeStampedModel, PersonalInformation):
    class Meta:
        verbose_name = 'Asiento'
        verbose_name_plural = 'Asientos'

    travel_schedule = models.ForeignKey(
        TravelsSchedule,
        on_delete=models.PROTECT,
        related_name="seatings",
        verbose_name='Horario de trayecto',
        null=True
    )
    seat_number = models.PositiveIntegerField(default=10, verbose_name='Número de asiento')

    def __str__(self):
        return "{} - {}".format(self.travel_schedule, self.seat_number)
