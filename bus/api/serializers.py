from rest_framework import serializers
from bus.models import Buses


class BusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buses
        exclude = ("created", "modified")


class CatalogBusesSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = Buses
        fields = ("id", "value")

    @staticmethod
    def get_value(obj):
        return "{}".format(obj)
