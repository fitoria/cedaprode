from django import forms
from django.contrib.auth.models import User
from models import * 

class RespuestaInlineForm(forms.ModelForm):
    pregunta = forms.ModelChoiceField(queryset = Pregunta.objects.all(), 
                                      widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(RespuestaInlineForm, self).__init__(*args, **kwargs)
        self.fields['respuesta'] = forms.ModelChoiceField(queryset = Opcion.objects.filter(pregunta=self.instance), 
                                      widget=forms.RadioSelect(), empty_label=None)
    
    class Meta:
        model = Respuesta

class EncuestaForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(queryset = User.objects.all(),
                                     widget=forms.HiddenInput)
    class Meta:
        model = Encuesta
