# Generated by Django 4.0.3 on 2022-04-11 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
        ('bus', '0001_initial'),
        ('travels', '0003_rename_end_data_travels_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travels',
            name='bus',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='travels',
            name='start_date',
        ),
        migrations.CreateModel(
            name='TravelsSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus_travels', to='bus.buses', verbose_name='Autobus')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='drivers.drivers', verbose_name='Conductor')),
            ],
            options={
                'verbose_name': 'Detalle de trayecto',
                'verbose_name_plural': 'Detalles de trayectos',
            },
        ),
    ]