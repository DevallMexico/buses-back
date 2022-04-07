from drivers.models import Drivers
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import DriversSerializer, CatalogDriversSerializer
from django.shortcuts import get_object_or_404


class DriversViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = DriversSerializer
    queryset = Drivers.objects.all()

    @action(methods=["get"], detail=False)
    def catalog(self, request):
        serializer = CatalogDriversSerializer(self.queryset, many=True)
        return Response(serializer.data)
