from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BikeRoute
from django.shortcuts import get_object_or_404
import json

def route_view(request, pk=None):
    """ Main view using Leaflet map in the template, allows for simple route selection"""
    polyline = [[[]]]
    all_routes = BikeRoute.objects.all()  # list of routes used for selection
    if pk:
        bike_route = get_object_or_404(all_routes, pk=pk)
        polyline = bike_route.polyline
        polyline = json.loads(polyline)  # convert string to a list

    template = loader.get_template('route/map.html')
    context = {
        'routes': all_routes,
        'polyline': polyline,
        'zoom': polyline[0][0][::-1]  # reverse coords for map.setView
               }
    return HttpResponse(template.render(context, request))

