from rest_framework import serializers
from seatings.models import Seatings


class SeatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seatings
        exclude = ()
