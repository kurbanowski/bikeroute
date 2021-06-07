from rest_framework import viewsets
from .models import BikeRoute
from .serializers import BikeRouteSerializer


class BikeRouteViewset(viewsets.ModelViewSet):
    """ Just the most basic implementation of DRF for the API"""
    queryset = BikeRoute.objects.all()
    serializer_class = BikeRouteSerializer
