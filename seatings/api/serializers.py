from rest_framework import serializers
from seatings.models import Seatings


class SeatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seatings
        exclude = ()

    @staticmethod
    def validate(data):
        seat_number = data["seat_number"]
        travel = data["travel_schedule"]
        seats_count = travel.seatings.filter(seat_number=seat_number).count()
        if seats_count > 0:
            raise serializers.ValidationError(
                "El asiento #{} ya no está disponible por favor escoge otro.".format(seat_number)
            )
        return data
