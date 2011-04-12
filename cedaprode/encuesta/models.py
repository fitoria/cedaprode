# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User

TIPOS_ORG = (('1', 'alcaldía'), ('2', 'sociedad civil'),
            ('3', 'gremios'), ('4', 'instituciones del estado'), 
            ('5', 'empresa'))

class Organizacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices = TIPOS_ORG)
    descripcion = models.TextField() 
    creado_por = models.ForeignKey(User)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #logo =  
    #departamento = models.ForeignKey(Departamento)

    class Meta:
        verbose_name_plural = 'Organizaciones'
        verbose_name = 'Organización'

    def __unicode__(self):
        return self.nombre

class Encuesta(models.Model):
    organizacion = models.ForeignKey(Organizacion)
    fecha = models.DateTimeField(auto_now_add = True)
    usuario = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        super(Encuesta, self).save(*args, **kwargs)
        #se registra cada pregunta en la encuesta
        for pregunta in Pregunta.objects.all():
            respuesta = Respuesta(pregunta = pregunta, encuesta = self)
            try:
                respuesta.save()
            except:
                pass

    def __unicode__(self):
        return 'Encuesta a %s con fecha %s' % (self.organizacion.nombre, self.fecha)

class Categoria(models.Model):
    '''Categoria principal'''
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = 'Categorías'

    def __unicode__(self):
        return self.titulo

class Pregunta(models.Model):
    categoria = models.ForeignKey(Categoria)
    titulo = models.CharField(max_length=200)
    texto_explicativo = models.TextField()

    def __unicode__(self):
        return self.titulo

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    titulo = models.CharField(max_length=200)
    puntaje = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Opciones'
        unique_together = ['pregunta', 'puntaje']

    def __unicode__(self):
        return '%s= %s' % (self.puntaje, self.titulo)

class Respuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta)
    pregunta = models.ForeignKey(Pregunta)
    respuesta = models.ForeignKey(Opcion, blank = True, null=True)
    comentario = models.TextField(blank=True, default='')

    class Meta:
        unique_together = ['encuesta', 'pregunta']

    def __unicode__(self):
        if self.respuesta:
            return '%s - %s(%s)' % (self.pregunta.titulo, 
                    self.respuesta.titulo, 
                    self.encuesta.usuario.username)
        else:
            return '%s - Sin responder(%s)' % (self.pregunta.titulo, 
                    self.encuesta.usuario.username)
