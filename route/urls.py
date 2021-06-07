from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.route_view, name='index_view'),
    url( r'^route/(?P<pk>\d+)/$', views.route_view, name = 'route_view')
]