from bus.models import Buses
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import BusesSerializer, CatalogBusesSerializer


class BusesViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = BusesSerializer
    queryset = Buses.objects.all()

    @action(methods=["get"], detail=False)
    def catalog(self, request):
        serializer = CatalogBusesSerializer(self.queryset, many=True)
        return Response(serializer.data)
