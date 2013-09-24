1. Cómo estructuro mi repo
--------------------------

Ejemplo de estructura:

.. code-block:: none

    README.rst
    LICENSE.txt

    setup.py
    MANIFEST.in

    requirements.txt

    simpleai/__init__.py
    simpleai/foo.py
    simpleai/bar.py

    docs/conf.py
    docs/index.rst
    docs/foo.rst

    tests/test_foo.py
    tests/test_bar.py

1. Cómo estructuro mi repo
--------------------------

Algunos consejos generales sobre dónde poner las cosas en el repo:

* El directorio que contiene nuestro paquete debe llamarse como el nombre del paquete, no cosas ambiguas como "src", "code", etc.
* El README es un **overview**, no es la doc completa. La doc va a estar en ``docs``.
* Tests y doc no suelen distribuirse dentro del paquete, están en directorios separados y no van a incluirse. 
* Y por esto tampoco es tan buena idea usar doctests, mejor hacer unittests.

Otros consejos sobre uso del versionado en sí:

* Separar branches de releases públicos, y de desarrollo. Es buena idea usar algo como **git-flow**, en lo que haya un branch para las versiones estables y otro para el desarrollo.
* Usar **tags** para marcar los releases! Así si alguien tiene instalada my_lib v1.5 puede encontrar fácilmente el código de esa versión. Y github también va a ofrecer cada tag como un release en la sección de descargas.

2. Cómo armo el paquete
-----------------------

* Hay varias herramientas: setuptools, distutils, distutils2, packaging, distribute.
* Packaging es lo mismo que distutils2 (fiu! una menos), y va a estar por default en python 3.
* Distutils viene por default en python 2.x.
* Por ahora elegimos **distutils**. A futuro puede que convenga pasar a **packaging** (distutils2).
* Peeeero, hay veces que distutils no se lleva bien con endpoints de paquetes hechos con setuptools, así que alguna vez puede que tengamos que pasar a setuptools (distutils no estará ya arreglado? habría que ver)

2. Cómo armo el paquete
-----------------------
 
Creamos un ``setup.py`` en la raíz del repo. Ejemplo básico:

.. code-block:: python

    from distutils.core import setup

    setup(
        name='simpleai',
        version='0.7.7',
        description=u'An implementation of AI algorithms based on aima-python',
        long_description=open('README.rst').read(),
        author = u'Juan Pedro Fisanotti',
        author_email = 'fisadev@gmail.com',
        url='http://github.com/simpleai-team/simpleai',
        packages=['simpleai', 'simpleai.search', 'simpleai.machine_learning'],
        package_data={'simpleai.search': ['web_viewer_resources/*.*']},
        license='LICENSE.txt',
        classifiers = [
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
        ],
    )

2. Cómo armo el paquete
-----------------------
 
* Distutils es bastante inteligente como para darse cuenta de qué cosas incluir de nuestros paquetes
* Pero a veces no es einstein, o puede que queramos incluir cosas extras. Es recomendable hacerlo explícito con un ``MANIFEST.in`` en la raíz del repo. Ejemplo:

.. code-block:: none
 
    include README.rst
    include LICENSE.txt
    recursive-include simpleai *.py
    recursive-include simpleai/search/web_viewer_resources *.*

3. Cómo distribuyo el paquete
-----------------------------

* Al tener un repo git la gente ya podría usar pip para instalar apuntando a la url del repo. 
* Pero es mejor subir el paquete a **PyPI** y que la gente pueda instalar con solo ``pip install my_lib``.
* Solo la primera vez, creamos un usuario en http://pypi.python.org y registramos el paquete:

.. code-block:: bash

    python setup.py register

* Cada vez que queremos subir una versión nueva, lo hacemos con:

.. code-block:: bash

    python setup.py sdist upload

* Hay más opciones, pero por lo general con eso estamos bien.

4. Cómo armo la doc
-------------------

* Lo más común es utilizar **sphinx** y escribir la doc en **ReST**, vamos a usar eso.
* Instalamos sphinx:

.. code-block:: bash

    sudo pip install sphinx

* Entramos al directorio ``docs``, e inicializamos sphinx (completando los datos que va pidiendo):

.. code-block:: bash

    sphinx-quickstart

* Cuando termina nos van a quedar un montón de archivos en el directorio de doc. 
* Completamos los archivos ``.rst`` con la doc en sí.
* Podemos probar compilar la doc a html para leerla localmente con algo como esto:

.. code-block:: bash

    make html
    google-chrome _build/html/index.html 

5. Cómo publico la doc
----------------------

* Nos creamos un usuario en http://readthedocs.org
* Registramos nuestro proyecto en el sitio.
* Dentro de readthedocs configuramos la url de nuestro repo, e indicando que la doc está en el directorio ``docs``.
* Si el repo está en **GitHub**, configuramos un service hook para que actualice readthedocs cada vez que pushemos versiones nuevas (si no podemos forzar las actualizaciones a mano).

6. Cómo ser feliz y tener una vida llena de sentido después de haber publicado un paquete como corresponde
----------------------------------------------------------------------------------------------------------

* Listo! Ya tenemos un repo bien estructurado, paquete de python armado y publicado, doc escrita con rst y que se publica sola.
* Cómo va a ser nuestro feliz trabajo diario?

  * Normalmente trabajamos y pusheamos sobre los branches de **desarrollo**.
  * Cuando tenemos algo **estable** como para releasear, actualizamos los números de versión en ``setup.py`` y ``docs/conf.py``, mergeamos al branch de stables, tageamos, y pusheamos.
  * Y después una cerveza o una coca, dependiendo del sujeto.

