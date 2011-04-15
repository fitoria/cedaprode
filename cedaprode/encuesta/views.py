from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.template import RequestContext
from forms import *
from decorators import checar_permiso
from models import *

@login_required
def inicio(request):
    return direct_to_template(request, 'index.html')

@login_required
@checar_permiso
def llenar_encuesta(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, pk = encuesta_id)
    preguntas = Pregunta.objects.all()
    PreguntaInlineFormSet = inlineformset_factory(Encuesta, Respuesta,
                                                  form=RespuestaInlineForm,
                                                  can_delete=False,
                                                  max_num=0)
    if request.method == 'POST':
        formset = PreguntaInlineFormSet(request.POST, request.FILES, instance = encuesta)
        if formset.is_valid():
            formset.save()
        else:
            formset = PreguntaInlineFormSet(request.POST, instance = encuesta)
    else:
        formset = PreguntaInlineFormSet(instance=encuesta)
    return render_to_response('encuesta/llenar_encuesta.html',
            {'formset': formset},
            context_instance=RequestContext(request))

@login_required
def crear_encuesta(request):
    encuesta = Encuesta(usuario=request.user)
    if request.method == 'POST':
        form = EncuestaForm(request.POST, instance=encuesta)
        if form.is_valid():
            encuesta = form.save(commit=False)
            encuesta.save()
            return redirect('llenar-encuesta', encuesta_id = encuesta.id)
    else:
        form = EncuestaForm(instance=encuesta)
    return render_to_response('encuesta/crear_encuesta.html',
                              {'form': form},
                              context_instance=RequestContext(request))

@login_required
def crear_organizacion(request):
    organizacion = Organizacion(creado_por=request.user)
    if request.method == 'POST':
        form = OrganizacionForm(request.POST, instance=organizacion)
        if form.is_valid():
            organizacion = form.save(commit=False)
            organizacion.save()
            #return redirect('llenar-encuesta', encuesta_id = encuesta.id)
    else:
        form = OrganizacionForm(instance=organizacion)
    return render_to_response('encuesta/crear_organizacion.html',
                              {'form': form},
                              context_instance=RequestContext(request))
