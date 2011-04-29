# -*- coding: UTF-8 -*-
from pygooglechart import RadarChart as Grafo

def generar_grafo(queryset, titulo):
    '''Genera un grafo a partir de un queryset o lista de respuestas'''
    data = []
    #legends = []
    labels = []
    for respuesta in queryset:
        data.append(int(respuesta.respuesta.puntaje))
        labels.append(respuesta.pregunta.titulo[:5])
        
    chart = Grafo(350, 350, auto_scale=True, x_range=(0,5), y_range=(0,5))
    chart.add_data(data)
    #chart.set_legend(['one', 'dos', 'tres', 'cuatro'])
    chart.set_title(titulo)
    #chart.set_grid(25 , 25, 4, 4)
    chart.set_axis_labels('x', labels)
    chart.set_axis_range('y', 0, 5)
    try:
        return chart.get_url()
    except:
        return 'http://i.imgur.com/gWDUH.jpg'
