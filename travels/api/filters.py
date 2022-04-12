import django_filters
from travels.models import TravelsSchedule


class TravelsScheduleFilter(django_filters.FilterSet):
    origin = django_filters.CharFilter(field_name="travel__origin", lookup_expr="icontains")
    destiny = django_filters.CharFilter(field_name="travel__destiny", lookup_expr="icontains")
    date = django_filters.CharFilter(field_name="start_date", lookup_expr="date")

    class Meta:
        model = TravelsSchedule
        fields = ("id",)

