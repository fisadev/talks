# coding: utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noticias.views.home', name='home'),
    # url(r'^noticias/', include('noticias.foo.urls')),

    url(r'^$', 'sitio.views.inicio', name='inicio'),
    url(r'^ver_noticia/(?P<noticia_id>\d+)/$', 'sitio.views.ver_noticia', name='ver_noticia'),
    url(r'^contacto/$', 'sitio.views.contacto', name='contacto'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
