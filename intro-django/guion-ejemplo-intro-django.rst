Parte 1: vista básica
=====================

* crear proyecto y aplicacion:

.. code-block::

    django-admin startproject noticias
    ./manage.py startapp sitio

* editar settings: path base de datos y cliente

* agregar aplicacion a INSTALLED_APPS:

.. code-block::

    'sitio',

* editar models:

.. code-block:: python

    class Categoria(models.Model):
        nombre = models.CharField(max_length=50)

    class Noticia(models.Model):
        titulo = models.CharField(max_length=50)
        texto = models.CharField(max_length=200)
        fecha = models.DateTimeField()
        archivada = models.BooleanField(default=False)
        categoria = models.ForeignKey(Categoria, blank=True, null=True, on_delete=models.CASCADE)

* crear directorio de templates
* crear template /noticias/sitio/templates/inicio.html:

.. code-block:: html

    <h1>noticias.com</h1>
    <p>bienvenido!</p>

* editar views:

.. code-block:: python

    def inicio(request):
        return render(request, 'inicio.html', {})

* editar urls:

.. code-block:: python

    from sitio import views


    path('inicio/', views.inicio),


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
    ./manage.py migrate

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

    from sitio.models import Noticia, Categoria

    @admin.register(Noticia)
    class AdminNoticia(admin.ModelAdmin):
        list_display = ('id', 'titulo', 'fecha', 'categoria')
        list_filter = ('archivada', 'fecha', 'categoria')
        search_fields = ('texto', )
        date_hierarchy = 'fecha'

    @admin.register(Categoria)
    class AdminCategoria(admin.ModelAdmin):
        list_display = ('id', 'nombre')


* crear superusuario si no existe

.. code-block:: bash

    ./manage.py createsuperuser

**web**


* editar models y volver a mostrar todo:


.. code-block:: python

    def __str__(self):
        return self.nombre


**web**

Parte 4: Error
==============

* hacer un error, levantar el server y ver que pasa


Parte 5: Consola
================

* mostrar queries y algo del estilo en la consola
