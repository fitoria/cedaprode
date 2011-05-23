from django import template
register = template.Library()
from django.conf import settings

@register.filter
def clasificador(value):
    base_url = '%s%s/' % (settings.MEDIA_URL, 'imagen')
    if value <= 36:
       return base_url + 'rojo.png'
    elif value <= 72:
       return base_url + 'naranja.png'
    elif value <= 108:
       return base_url + 'amarillo.png'
    elif value <= 144:
       return base_url + 'verde.png'
    elif value <= 180:
       return base_url + 'azul.png'
    else:
        raise Exception('la shit no es correcta')

@register.filter
def categorizador(value):
    '''Value es el formset'''
    resultados = []
    fila = {'categoria': None, 'forms': []}
    for index, form in enumerate(value):
        if fila['categoria'] == None:
            fila['categoria'] = form.instance.pregunta.categoria
            fila['forms'].append(form)
        elif fila['categoria'] != form.instance.pregunta.categoria:
            resultados.append(dict.copy(fila))
            fila['categoria'] = form.instance.pregunta.categoria
            fila['forms'] = [form]
        elif fila['categoria'] == form.instance.pregunta.categoria:
            fila['forms'].append(form)
            #para que aparezca el fucking paso nueve
            if index == len(value) -1 :
                resultados.append(dict.copy(fila))

    return resultados
