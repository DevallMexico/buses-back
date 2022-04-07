from travels.models import Travels
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TravelsSerializer, ListTravelSerializer
from django.shortcuts import get_object_or_404


class TravelsViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Travels.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ListTravelSerializer
        if self.action in ("partial_update", "create", "delete"):
            return TravelsSerializer
