# -*- coding: UTF-8 -*-
from django.db import models

class Categoria(models.Model):
    '''Categoria principal'''
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = 'Categorías'

    def __unicode__(self):
        return self.titulo

class Pregunta(models.Model):
    titulo = models.CharField(max_length=200)
    texto_explicativo = models.TextField()

    def __unicode__(self):
        return self.titulo

class Opcion(models.Model):
    titulo = models.CharField(max_length=200)
    puntaje = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Opciones'

    def __unicode__(self):
        return '%s= %s' % (self.puntaje, self.titulo)
