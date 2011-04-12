# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Organizacion'
        db.create_table('encuesta_organizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('creado_por', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('encuesta', ['Organizacion'])

        # Adding model 'Encuesta'
        db.create_table('encuesta_encuesta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Organizacion'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('encuesta', ['Encuesta'])

        # Adding model 'Categoria'
        db.create_table('encuesta_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('encuesta', ['Categoria'])

        # Adding model 'Pregunta'
        db.create_table('encuesta_pregunta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Categoria'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('texto_explicativo', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('encuesta', ['Pregunta'])

        # Adding model 'Opcion'
        db.create_table('encuesta_opcion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Pregunta'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('puntaje', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('encuesta', ['Opcion'])

        # Adding unique constraint on 'Opcion', fields ['pregunta', 'puntaje']
        db.create_unique('encuesta_opcion', ['pregunta_id', 'puntaje'])

        # Adding model 'Respuesta'
        db.create_table('encuesta_respuesta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuesta'])),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Pregunta'])),
            ('respuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Opcion'], null=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal('encuesta', ['Respuesta'])

        # Adding unique constraint on 'Respuesta', fields ['encuesta', 'pregunta']
        db.create_unique('encuesta_respuesta', ['encuesta_id', 'pregunta_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Respuesta', fields ['encuesta', 'pregunta']
        db.delete_unique('encuesta_respuesta', ['encuesta_id', 'pregunta_id'])

        # Removing unique constraint on 'Opcion', fields ['pregunta', 'puntaje']
        db.delete_unique('encuesta_opcion', ['pregunta_id', 'puntaje'])

        # Deleting model 'Organizacion'
        db.delete_table('encuesta_organizacion')

        # Deleting model 'Encuesta'
        db.delete_table('encuesta_encuesta')

        # Deleting model 'Categoria'
        db.delete_table('encuesta_categoria')

        # Deleting model 'Pregunta'
        db.delete_table('encuesta_pregunta')

        # Deleting model 'Opcion'
        db.delete_table('encuesta_opcion')

        # Deleting model 'Respuesta'
        db.delete_table('encuesta_respuesta')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Organizacion']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'encuesta.opcion': {
            'Meta': {'unique_together': "(['pregunta', 'puntaje'],)", 'object_name': 'Opcion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Pregunta']"}),
            'puntaje': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'creado_por': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'encuesta.pregunta': {
            'Meta': {'object_name': 'Pregunta'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Categoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto_explicativo': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.respuesta': {
            'Meta': {'unique_together': "(['encuesta', 'pregunta'],)", 'object_name': 'Respuesta'},
            'comentario': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuesta']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Pregunta']"}),
            'respuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Opcion']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['encuesta']
