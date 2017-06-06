from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<channel>\w+)/$', views.channel, name='channel'),
]
