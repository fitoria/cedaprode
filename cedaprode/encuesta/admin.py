# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import *

class OpcionInline(admin.TabularInline):
    model = Opcion
    max_num = 5

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]

admin.site.register(Categoria)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
admin.site.register(Organizacion)
admin.site.register(Encuesta)
admin.site.register(Adjunto)
