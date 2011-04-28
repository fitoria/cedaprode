# -*- coding: UTF-8 -*-
from pygooglechart import SplineRadarChart as Grafo

def generar_grafo(queryset, titulo):
    '''Genera un grafo a partir de un queryset o lista de respuestas'''
    data = []
    #legends = []
    labels = []
    for respuesta in queryset:
        data.append(int(respuesta.respuesta.puntaje))
        labels.append(respuesta.pregunta.titulo[:5])
        
    chart = Grafo(250, 250)
    chart.add_data(data)
    #chart.set_legend(['one', 'dos', 'tres', 'cuatro'])
    chart.set_title(titulo)
    chart.set_grid(10,10, 5, 5)
    chart.set_axis_labels('x', labels)
    return chart.get_url()
