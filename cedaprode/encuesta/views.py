# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.template import RequestContext
from django.db.models import Sum
from forms import *
from decorators import checar_permiso
from models import *
from utils import generar_grafo

def index(request):
    if request.user.is_authenticated():
        return redirect('inicio')
    else:
        return redirect('user-login')

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
            return redirect('organizacion-detalle', pk=organizacion.id)
    else:
        form = OrganizacionForm(instance=organizacion)
    return render_to_response('encuesta/crear_organizacion.html',
                              {'form': form},
                              context_instance=RequestContext(request))

@login_required
def editar_organizacion(request, organizacion_id):
    organizacion = get_object_or_404(Organizacion, creado_por=request.user, pk=organizacion_id)
    if request.method == 'POST':
        form = OrganizacionForm(request.POST, instance=organizacion)
        if form.is_valid():
            organizacion = form.save(commit=False)
            organizacion.save()
            return redirect('organizaciones')
    else:
        form = OrganizacionForm(instance=organizacion)
    return render_to_response('encuesta/editar_organizacion.html',
                              {'form': form},
                              context_instance=RequestContext(request))

@login_required
def mis_encuestas(request):
    encuestas = Encuesta.objects.filter(usuario = request.user).order_by('organizacion')
    return render_to_response('encuesta/mis_encuestas.html', {'encuestas': encuestas},
                              context_instance=RequestContext(request))

@login_required
def resultado(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, pk=encuesta_id)
    #lista que tendra todos los resultados...
    resultados = []
    for categoria in Categoria.objects.all():
        puntaje = Respuesta.objects.filter(encuesta=encuesta,
                                           pregunta__categoria=categoria).aggregate(total=Sum('respuesta__puntaje'))['total']
        fila = {'categoria': categoria, 'puntaje': puntaje}
        respuestas = []
        for pregunta in Pregunta.objects.filter(categoria = categoria):
            respuesta = Respuesta.objects.get(encuesta = encuesta,
                                                  pregunta = pregunta)
            respuestas.append(respuesta)
        grafo_url = generar_grafo(respuestas, categoria.titulo)
        fila['respuestas'] = respuestas
        fila['grafo_url'] = grafo_url
        fila['total_maximo'] = len(respuestas) * 5
        resultados.append(fila)

    return render_to_response('encuesta/resultado.html',
                              {'encuesta': encuesta, 'resultados': resultados},
                              context_instance=RequestContext(request))

#@login_required
#def resultado_consolidado(request, encuesta_id):
#    encuesta = get_object_or_404(Encuesta, pk=encuesta_id)
#    for categoria in Categoria.objects.all():
#        puntaje

@login_required
def resultados(request):
    if request.method == 'POST':
        form = BuscarResultadoForm(request.POST)
        if form.is_valid():
            encuestas = Encuesta.objects.filter(organizacion__tipo = form.cleaned_data['tipo'])
    else:
        form = BuscarResultadoForm()
        encuestas = Encuesta.objects.filter(usuario = request.user)

    return render_to_response('encuesta/resultados.html', 
                              {'encuestas': encuestas, 'form': form},
                              context_instance=RequestContext(request))

@login_required
def organizaciones(request):
    organizaciones = Organizacion.objects.filter(creado_por=request.user)
    #form = BuscarForm()

    return render_to_response('encuesta/organizacion_list.html',
                              {'object_list': organizaciones},
                              #{'object_list': organizaciones, 'form': form},
                              context_instance=RequestContext(request))

@login_required
def buscar_orgs(request):
    if request.method == "POST":
        form = BuscarForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['tipo'] and form.cleaned_data['municipio']:
                resultados = Organizacion.objects.filter(tipo = form.cleaned_data['tipo'],municipio = form.cleaned_data['municipio'])
            elif form.cleaned_data['tipo']: 
                resultados = Organizacion.objects.filter(tipo = form.cleaned_data['tipo'])
            elif form.cleaned_data['municipio']: 
                resultados = Organizacion.objects.filter(tipo = form.cleaned_data['municipio'])

            return render_to_response('encuesta/buscar_orgs.html',
                              {'organizaciones': resultados, 'form': form},
                              context_instance=RequestContext(request))
    else:
        form = BuscarForm()
        return render_to_response('encuesta/buscar_orgs.html',
                          {'form': form},
                          context_instance=RequestContext(request))
