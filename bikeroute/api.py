from rest_framework import routers
from route import api_views

router = routers.DefaultRouter()
router.register(r'route', api_views.BikeRouteViewset)