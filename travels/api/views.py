from travels.models import Travels, TravelsSchedule
from rest_framework import status, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TravelsSerializer, ListTravelScheduleSerializer, TravelScheduleSerializer
from django.shortcuts import get_object_or_404
from .filters import TravelsScheduleFilter


class TravelsViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer


class TravelSchedulesViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = TravelsSchedule.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TravelsScheduleFilter

    def get_serializer_class(self):
        if self.action == "list":
            return ListTravelScheduleSerializer
        if self.action in ("partial_update", "create", "delete"):
            return TravelScheduleSerializer
