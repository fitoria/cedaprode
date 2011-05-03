from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import ListView, DetailView
from models import Organizacion


urlpatterns = patterns('encuesta.views',
            url(r'^mis-encuestas/$', 'mis_encuestas', name='mis-encuestas'),
            url(r'^llenar-encuesta/(?P<encuesta_id>\d+)/$', 'llenar_encuesta', name='llenar-encuesta'),
            url(r'^crear-encuesta/$', 'crear_encuesta', name='crear-encuesta'),
            url(r'^crear-organizacion/$', 'crear_organizacion', name='crear-organizacion'),
            url(r'^editar-organizacion/(?P<organizacion_id>\d+)/$', 'editar_organizacion', name='editar-organizacion'),
            url(r'^organizaciones/$', ListView.as_view(model=Organizacion), name='organizaciones'),
            url(r'^organizacion/(?P<pk>\d+)/$', 
                DetailView.as_view(model=Organizacion, template_name='encuesta/organizacion.html'), 
                name='organizacion-detalle'),
            url(r'^resultado/(?P<encuesta_id>\d+)/$', 'resultado', name='resultado'),
            url(r'^resultados/$', 'resultados', name='resultados'),
            url(r'^inicio/$', 'inicio', name='inicio'),
            url(r'^$', 'index'),
            )
