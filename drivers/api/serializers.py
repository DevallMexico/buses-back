from rest_framework import serializers
from drivers.models import Drivers


class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        exclude = ("created", "modified")


class CatalogDriversSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = Drivers
        fields = ("id", "value")

    def get_value(self, obj):
        return "{}".format(obj)

