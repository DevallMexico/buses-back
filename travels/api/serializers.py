from rest_framework import serializers
from travels.models import Travels
from bus.api.serializers import BusesSerializer
from drivers.api.serializers import DriversSerializer


class TravelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Travels
        exclude = ()


class ListTravelSerializer(serializers.ModelSerializer):
    bus = BusesSerializer(read_only=True)
    driver = DriversSerializer(read_only=True)

    class Meta:
        model = Travels
        exclude = ()

