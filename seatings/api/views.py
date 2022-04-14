from seatings.models import Seatings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SeatingsSerializer
from .filters import SeatingsFilter
from django.db import transaction, IntegrityError
from rest_framework.exceptions import ValidationError


class SeatingsViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = SeatingsSerializer
    queryset = Seatings.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SeatingsFilter

    @action(methods=["post"], detail=False)
    def multiple(self, request):
        seat_number = 0
        try:
            with transaction.atomic():
                data = request.data
                for seat in data["seatings"]:
                    seat["travel_schedule"] = data["travel_schedule"]
                    seat_number = seat["seat_number"]
                    seatings_serializer = SeatingsSerializer(data=seat)
                    if seatings_serializer.is_valid():
                        seatings_serializer.save()
                    else:
                        raise ValidationError
            return Response({"status": True})
        except ValidationError:
            return Response({
                "status": False,
                "message": "El asiento #{} ya no está disponible por favor escoge otro.".format(seat_number),
            })
