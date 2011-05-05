from models import Organizacion

def sidebar(request):
    if request.user.is_authenticated():
        user = request.user
        orgs = Organizacion.objects.filter(creado_por = user)
        return {'user': user, 'orgs': orgs, 'logueado': True}
    else:
        return {'logueado': False}
