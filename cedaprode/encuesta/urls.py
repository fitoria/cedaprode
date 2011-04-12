from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('encuesta.views',
            url(r'^llenar-encuesta/(?P<encuesta_id>\d+)/$', 'llenar_encuesta', name='llenar-encuesta'),
            url(r'^crear-encuesta/$', 'crear_encuesta', name='crear-encuesta'),
            url(r'^crear-organizacion/$', 'crear_organizacion', name='crear-organizacion'),
            )
