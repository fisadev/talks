# coding: utf-8
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    fecha = models.DateTimeField(db_index=True)
    archivada = models.BooleanField()
    categoria = models.ForeignKey(Categoria, related_name='noticias')

    def __unicode__(self):
        return self.titulo


class Comentario(models.Model):
    texto = models.TextField()
    noticia = models.ForeignKey(Noticia, related_name='comentarios')
    fecha = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "(%s) %s..." % (self.fecha, self.texto[:15])


@receiver(models.signals.post_save, sender=Comentario)
def my_handler(sender, instance, **kwargs):
    send_mail('Nuevo comentario en noticia: ' + instance.noticia.titulo,
              instance.texto,
              'sitio@noticias.com',
              ['community_manager@noticias.com'])
