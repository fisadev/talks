# coding: utf-8
from datetime import date

from django.db import transaction
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from sitio.models import Noticia
from sitio.forms import ContactoForm, ComentarioForm


def inicio(request):
    lista_noticias = Noticia.objects.exclude(archivada=True)\
                                    .order_by('-fecha')

    return render_to_response('inicio.html',
                              {'lista_noticias': lista_noticias},
                              context_instance=RequestContext(request))


def ver_noticia(request, noticia_id):
    noticia = Noticia.objects.get(pk=noticia_id)

    form = ComentarioForm(request.POST or None)

    if form.is_valid():
        nuevo_comentario = form.save(commit=False)
        nuevo_comentario.noticia = noticia
        nuevo_comentario.save()

        form = ComentarioForm()

    return render_to_response('ver_noticia.html',
                              {'noticia': noticia,
                               'form': form},
                              context_instance=RequestContext(request))


def contacto(request):
    form = ContactoForm(request.POST or None)

    if form.is_valid():
        send_mail(form.cleaned_data['titulo'],
                  form.cleaned_data['texto'],
                  'sitio@noticias.com',
                  ['community_manager@noticias.com'])

        return HttpResponseRedirect(reverse('inicio'))

    return render_to_response('contacto.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def archivar_viejas(request):
    for noticia in Noticia.objects.filter(archivada=False, fecha__lt=date.today()):
        noticia.archivada = True
        noticia.save()

    return render_to_response('ok.html')
