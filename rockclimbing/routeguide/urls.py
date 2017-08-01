from django.conf.urls import url, include
from . import views

app_name = 'routeguide'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^indoor/$', views.indoor, name='indoor'),
    url(r'indoor/(?P<gym_id>[0-9]+)/$', views.indoor_gym, name='indoor_gym'),
]