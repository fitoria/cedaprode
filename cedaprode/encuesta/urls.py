from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.views.generic.simple import direct_to_template
from models import Organizacion

urlpatterns = patterns('encuesta.views',
            url(r'^mis-encuestas/$', 'mis_encuestas', name='mis-encuestas'),
            url(r'^llenar-encuesta/(?P<encuesta_id>\d+)/$', 'llenar_encuesta', name='llenar-encuesta'),
            url(r'^adjuntar/(?P<encuesta_id>\d+)/$', 'adjuntar', name='adjuntar'),
            url(r'^crear-encuesta/$', 'crear_encuesta', name='crear-encuesta'),
            url(r'^crear-organizacion/$', 'crear_organizacion', name='crear-organizacion'),
            url(r'^editar-organizacion/(?P<organizacion_id>\d+)/$', 'editar_organizacion', name='editar-organizacion'),
            url(r'^organizaciones/$', 'organizaciones', name='organizaciones'),
            url(r'^organizacion/(?P<pk>\d+)/$', 
                DetailView.as_view(model=Organizacion, template_name='encuesta/organizacion.html'), 
                name='organizacion-detalle'),
            url(r'^resultado/(?P<encuesta_id>\d+)/adjuntos/$', 'ver_adjuntos', name='ver-adjuntos'),
            url(r'^resultado/(?P<encuesta_id>\d+)/imprimir/$', 'resultado', 
                {'template_name': 'imprimir.html'}, name='imprimir'),
            url(r'^resultado/(?P<encuesta_id>\d+)/eliminar/$', 'eliminar_encuesta', name='eliminar'),
            url(r'^resultado/(?P<encuesta_id>\d+)/$', 'resultado',
                {'template_name': 'resultado.html'}, name='resultado'),
            url(r'^buscar-orgs/$', 'buscar_orgs', name='buscar-orgs'),
            url(r'^resultados/$', 'resultados', name='resultados'),
            url(r'^inicio/$', 'inicio', name='inicio'),
            url(r'^ayuda/$', direct_to_template, {'template': 'encuesta/ayuda.html'}, name='ayuda'),
            url(r'^$', 'index'),
            )
