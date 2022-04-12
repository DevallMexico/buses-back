from rest_framework import serializers
from travels.models import Travels, TravelsSchedule
from bus.api.serializers import BusesSerializer
from drivers.api.serializers import DriversSerializer


class TravelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travels
        exclude = ()


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


