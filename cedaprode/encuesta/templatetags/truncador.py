from django import template
register = template.Library()

@register.filter
def truncador(value, arg):
    try:
        arg = int(arg)
    except:
        raise Exception('arg must be an Integer')

    return ' '.join(value.split(' ')[:arg])
