from seatings.models import Seatings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SeatingsSerializer
from django.shortcuts import get_object_or_404
from .filters import SeatingsFilter


class SeatingsViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = SeatingsSerializer
    queryset = Seatings.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SeatingsFilter

    @action(methods=["post"], detail=False)
    def multiple(self, request):
        try:
            data = request.data
            for seat in data["seatings"]:
                seat["travel_schedule"] = data["travel_schedule"]
                seatings_serializer = SeatingsSerializer(data=seat)
                if seatings_serializer.is_valid():
                    seatings_serializer.save()
            return Response({"status": True})
        except Exception as error:
            return Response({"status": False, "message": error})
