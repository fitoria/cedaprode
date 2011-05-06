# -*- coding: UTF-8 -*-
from pygooglechart import RadarChart as Grafo

def generar_grafo(queryset, titulo):
    '''Genera un grafo a partir de un queryset o lista de respuestas'''
    data = []
    legends = []
    labels = []
    for respuesta in queryset:
        try:
            data.append(int(respuesta.respuesta.puntaje))
            labels.append(respuesta.pregunta.titulo[:2])
            legends.append(respuesta.pregunta.titulo[:50])
        except:
            pass

    if len(data) > 2:
        data.append(data[0])

    chart = Grafo(600, 350, auto_scale=True, x_range=(0,5), y_range=(0,5))
    chart.add_data(data)
    chart.set_title(titulo)
    chart.set_legend(legends)
    chart.set_legend_position('r')
    chart.set_axis_labels('x', labels)
    chart.set_axis_range('y', 0, 5)
    try:
        return chart.get_url()
    except:
        return '/files/imagen/grafoerror.jpg'

def generar_grafro_general(titulo, filas, ejes):
    chart = Grafo(600, 350, auto_scale=True, x_range=(0,100), y_range=(0,100))
    filas.append(filas[0])
    chart.add_data(filas)
    chart.set_title(titulo)
    chart.set_axis_labels('x', range(1, len(ejes)+ 1))
    legends = [(str(i+1) + '-' + j) for i, j in enumerate(ejes)] 
    chart.set_legend(legends)
    chart.set_axis_range('y', 0, 30)
    try:
        return chart.get_url()
    except:
        return '/files/imagen/grafoerror.jpg'
