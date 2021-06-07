from django.db import models
from djgeojson.fields import LineStringField

class BikeRoute(models.Model):
    """ Simple model with custom route name and polylinestring"""
    name = models.CharField(default='NoName', max_length=256)
    polyline = LineStringField()