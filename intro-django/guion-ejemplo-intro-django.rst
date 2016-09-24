Parte 1: vista básica
=====================

* crear proyecto y aplicacion:

.. code-block::

    django-admin.py startproject noticias
    ./manage.py startapp sitio

* editar settings: path base de datos y cliente

* agregar aplicacion a INSTALLED_APPS:

.. code-block::

    'sitio',

* editar models:

.. code-block:: python

    class Noticia(models.Model):
        titulo = models.CharField(max_length=50)
        texto = models.CharField(max_length=200)
        fecha = models.DateTimeField()
        archivada = models.BooleanField(default=False)

* crear directorio de templates
* crear template /noticias/sitio/templates/inicio.html:

.. code-block:: html

    <h1>Noticias.com</h1>
    <p>bienvenido!</p>

* editar views:

.. code-block:: python

    def inicio(request):
        return render(request, 'inicio.html', {})

* editar urls:

.. code-block:: python

    url(r'^inicio/$', 'sitio.views.inicio'),

* levantar servidor y probar:

.. code-block::

    ./manage.py runserver

**web**

http://localhost:8000/inicio

Parte 2: Modelos
================

* editar views:

.. code-block:: python

    from sitio.models import Noticia
    from datetime import datetime


    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

* sincronizar base de datos:

.. code-block::

    ./manage.py makemigrations
    ./manage.py syncdb

**web**

* modificar template inicio:

.. code-block:: html

    {% for noticia in lista_noticias %}
        <h3>{{ noticia.fecha }} {{ noticia.titulo }}</h3>
        <p>{{ noticia.texto }}</p>
    {% endfor %}

* modificar views:

.. code-block:: python

    noticias = Noticia.objects.all()
    return render(request, 'inicio.html', {'lista_noticias': noticias})

**web**

Parte 3: Admin
==============

* editar admin.py:

.. code-block:: python

    from sitio.models import Noticia
    
    admin.site.register(Noticia)

* crear superusuario si no existe

.. code-block:: bash

    ./manage.py createsuperuser

**web**

* customizar el admin.py:

.. code-block:: python

    class AdminNoticia(admin.ModelAdmin):
        list_display = ('id', 'titulo', 'fecha',)
        list_filter = ('archivada', 'fecha')
        search_fields = ('texto', )
        date_hierarchy = 'fecha'

    admin.site.register(Noticia, AdminNoticia)

**web**

Parte 4: Error
==============

* hacer un error, levantar el server y ver que pasa
