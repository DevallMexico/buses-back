import django_filters
from seatings.models import Seatings


class SeatingsFilter(django_filters.FilterSet):
    travel = django_filters.CharFilter(field_name="travel_schedule__id")

    class Meta:
        model = Seatings
        fields = ("id",)

