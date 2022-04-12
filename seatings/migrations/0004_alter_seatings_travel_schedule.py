# Generated by Django 4.0.3 on 2022-04-11 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0005_travelsschedule_travel'),
        ('seatings', '0003_seatings_travel_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seatings',
            name='travel_schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='travel_schedule', to='travels.travelsschedule', verbose_name='Horario de trayecto'),
        ),
    ]
