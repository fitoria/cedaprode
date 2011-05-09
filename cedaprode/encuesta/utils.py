# -*- coding: UTF-8 -*-
from pygooglechart import StackedHorizontalBarChart as Barra, RadarChart as Grafo

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
    chart.set_line_style(0, 2)
    try:
        return chart.get_url()
    except:
        return '/files/imagen/grafoerror.jpg'

def generar_grafro_general(titulo, filas, ejes):
    return dict(barra=generar_grafo_barra(titulo, filas, ejes),
                radar=generar_grafo_radar_norm(titulo, filas, ejes))

def generar_grafo_barra(titulo, filas, ejes):
    chart = Barra(620, 340, auto_scale=True, x_range=(0,30), y_range=(0,30))
    #filas.append(filas[0])
    chart.set_colours(['00ff00', 'ff0000'])
    chart.add_data([f[0] for f in filas])
    chart.add_data([f[1] for f in filas])
    chart.set_title(titulo)
    #chart.set_axis_labels('x', range(1, len(ejes)+ 1))
    legends = ['%s (%s/%s)' % (i, j[0], j[1]) for i, j in zip(ejes, filas)] 
    chart.set_axis_labels('y', legends)
    #chart.set_legend(legends)
    chart.set_legend(['Puntaje alcanzado', 'Total posible'])
    chart.set_axis_range('x', 0, 30)
    chart.set_line_style(0, 2)
    try:
        return chart.get_url()
    except:
        return '/files/imagen/grafoerror.jpg'

def generar_grafo_radar_norm(titulo, filas, ejes):
    chart = Grafo(600, 350, auto_scale=True, x_range=(0,100), y_range=(0,100))
    #normalizamos valores
    saca_porcentaje = lambda x : (float(x[0])/x[1]) * 100
    fila_normalizada = map(saca_porcentaje, filas)
    fila_normalizada.append(fila_normalizada[0])
    chart.add_data(fila_normalizada)
    chart.set_title(titulo)
    chart.set_axis_labels('x', range(1, len(ejes)+ 1))
    legends = [(str(i+1) + '-' + j) for i, j in enumerate(ejes)] 
    chart.set_legend(legends)
    chart.set_axis_range('y', 0, 100)
    chart.set_line_style(0, 2)
    try:
        return chart.get_url()
    except:
        return '/files/imagen/grafoerror.jpg'
