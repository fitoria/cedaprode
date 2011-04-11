from models import Encuesta
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def checar_permiso(f):
    def checarlo(request, **kwargs):
        if kwargs['encuesta_id']:
            encuesta = Encuesta.objects.get(pk=kwargs['encuesta_id'])
            if encuesta.usuario != request.user:
                return HttpResponseRedirect('/')
            return f(request, **kwargs)
    return checarlo
