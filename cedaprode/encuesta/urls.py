from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('encuesta.views',
            (r'^formulario/(?P<encuesta_id>\d+)/$', 'formulario'),
            )
