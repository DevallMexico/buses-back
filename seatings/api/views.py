from seatings.models import Seatings
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import SeatingsSerializer
from django.shortcuts import get_object_or_404


class SeatingsViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = SeatingsSerializer
    queryset = Seatings.objects.all()
