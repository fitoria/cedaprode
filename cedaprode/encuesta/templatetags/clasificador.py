from django import template
register = template.Library()
from django.conf import settings

@register.filter
def clasificador(value):
    base_url = '%s%s/' % (settings.MEDIA_URL, 'imagen')
    if value <= 60:
       return base_url + 'amarillo.png'
    elif value <= 120:
       return base_url + 'verde.png'
    elif value > 150:
       return base_url + 'azul.png'
    else:
        raise Exception('la shit no es correcta')
