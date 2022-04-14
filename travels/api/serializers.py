import datetime
import pytz
from rest_framework import serializers
from travels.models import Travels, TravelsSchedule
from bus.api.serializers import BusesSerializer
from drivers.api.serializers import DriversSerializer
from django.db.models import Count, Q, F, ExpressionWrapper, FloatField, Sum, Case, Value, When
from django.db.models.functions import Coalesce

utc = pytz.UTC


class TravelsSerializer(serializers.ModelSerializer):
    avg_passengers_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Travels
        exclude = ()

    @staticmethod
    def get_avg_passengers_percentage(obj):
        queryset = obj.travel_schedules.all()
        total_capacity = queryset.aggregate(
            total_capacity=Coalesce(Sum("bus__capacity"), 0)
        )["total_capacity"]
        total_seats = queryset.aggregate(total_seats=Count("seatings__pk"))["total_seats"]
        if total_capacity > 0:
            return (total_seats * 100) / total_capacity
        return 0


class ListTravelScheduleSerializer(serializers.ModelSerializer):
    bus = BusesSerializer(read_only=True)
    driver = DriversSerializer(read_only=True)
    travel = TravelsSerializer(read_only=True)
    avg_percentage = serializers.SerializerMethodField()

    class Meta:
        model = TravelsSchedule
        exclude = ()

    @staticmethod
    def get_avg_percentage(obj):
        seatings_count = obj.seatings.all().count()
        percentage = (seatings_count * 100) / obj.bus.capacity
        return "{:.2f}%".format(percentage)


class TravelScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelsSchedule
        exclude = ()

    @staticmethod
    def validate(data):
        start_date = data["start_date"].replace(tzinfo=utc)
        end_date = data["end_date"].replace(tzinfo=utc)
        today = datetime.datetime.today().replace(tzinfo=utc)
        if start_date <= today:
            raise serializers.ValidationError("La hora y día de salida no puede ser menor a la fecha y día actual")
        if end_date <= start_date:
            raise serializers.ValidationError("La hora y día de llegada no puede ser menor a la fecha y dáa de salida")
        return data


