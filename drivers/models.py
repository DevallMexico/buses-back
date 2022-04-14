from django.db import models
from users.models import TimeStampedModel

# Create your models here.

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre(s)')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    age = models.PositiveIntegerField(verbose_name='Edad')

    class Meta:
        abstract = True


class Drivers(TimeStampedModel, PersonalInformation):
    class Meta:
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'

    cel_phone = models.CharField(null=True, max_length=15)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
