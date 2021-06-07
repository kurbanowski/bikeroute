from rest_framework import serializers
from . import models

class BikeRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BikeRoute
        fields = ('id', 'name', 'polyline')