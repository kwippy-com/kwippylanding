from django.conf.urls.defaults import *

urlpatterns = patterns('miscproject.comingsoon.views',
      (r'^$', 'coming_soon'),
      (r'^$/', 'coming_soon')
)
