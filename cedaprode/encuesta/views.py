from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from models import *

def formulario(request, encuesta_id):
    encuesta = get_object_or_404(Encuesta, pk = encuesta_id)
    preguntas = Pregunta.objects.all()
    PreguntaInlineFormSet = inlineformset_factory(Encuesta, Respuesta, can_delete=False)
    if request.method == 'POST':
        formset = PreguntaInlineFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
        else:
            formset = PreguntaInlineFormSet(instance = encuesta)
    else:
        formset = PreguntaInlineFormSet(instance=encuesta)
    return render_to_response('encuesta/formulario.html', {'formset': formset})
