from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.channel, name='channel'),
    url(r'^$', views.index, name='index'),
    url(r'^replay/$', views.replay, name='replay'),
    url(r'^(?P<slug>[\w-]+)/$', views.channel, name='channel'),
]
