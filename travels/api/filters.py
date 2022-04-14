import django_filters
from travels.models import TravelsSchedule
from django.db.models import Count, Q, F, ExpressionWrapper, FloatField

class TravelsScheduleFilter(django_filters.FilterSet):
    date = django_filters.CharFilter(field_name="start_date", lookup_expr="date")
    travel = django_filters.CharFilter(field_name="travel__id")
    sold_capacity = django_filters.NumberFilter(method='get_sold_capacity')

    class Meta:
        model = TravelsSchedule
        fields = ("id",)

    @staticmethod
    def get_sold_capacity(queryset, name, value):
        if value:
            return queryset.annotate(
                total_seats=Count("seatings__pk"),
                percentage_avg=ExpressionWrapper(
                    (F('total_seats') * 100) / F("bus__capacity"),
                    output_field=FloatField()
                )
            ).filter(percentage_avg__gte=value)
        return queryset


