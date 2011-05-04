from django import forms
from django.contrib.auth.models import User
from models import * 

class RespuestaInlineForm(forms.ModelForm):
    pregunta = forms.ModelChoiceField(queryset = Pregunta.objects.all(), 
                                      widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(RespuestaInlineForm, self).__init__(*args, **kwargs)
        self.fields['respuesta'] = forms.ModelChoiceField(queryset = Opcion.objects.filter(pregunta=self.instance.pregunta), 
                                      widget=forms.RadioSelect(), empty_label=None, required=False)
    
    class Meta:
        model = Respuesta

class EncuestaForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset = User.objects.all(),
                                     widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(EncuestaForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['organizacion'] = forms.ModelChoiceField(queryset = Organizacion.objects.filter(creado_por=self.instance.usuario))
    
    class Meta:
        model = Encuesta

class OrganizacionForm(forms.ModelForm):
    creado_por = forms.ModelChoiceField(queryset = User.objects.all(),
                                     widget=forms.HiddenInput)

    class Meta:
        model = Organizacion

class BuscarForm(forms.Form):
    municipio = forms.ModelChoiceField(queryset = Municipio.objects.all())
    tipo = forms.ChoiceField(choices = TIPOS_ORG)
