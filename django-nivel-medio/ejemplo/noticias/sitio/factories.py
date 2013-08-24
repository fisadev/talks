# coding: utf-8
from datetime import datetime
import factory

from sitio.models import Categoria, Noticia


class CategoriaFactory(factory.Factory):
    FACTORY_FOR = Categoria
    nombre = factory.Sequence(lambda n: 'categoria {0}'.format(n))


class NoticiaFactory(factory.Factory):
    FACTORY_FOR = Noticia
    titulo = factory.Sequence(lambda n: 'noticia {0}'.format(n))
    fecha = datetime.now()
    categoria = factory.SubFactory(CategoriaFactory)
