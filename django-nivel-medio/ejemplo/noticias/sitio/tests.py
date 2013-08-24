# coding: utf-8
from django.test import TestCase

from sitio.models import Noticia


class SimpleTest(TestCase):
    def test_la_matematica_no_se_rompio(self):
        self.assertEqual(1 + 1, 2)


class AlsoSimpleTest(TestCase):
    def test_inicio_tiene_todas_las_noticias(self):
        n1 = NoticiaFactory()
        n2 = NoticiaFactory()

        response = self.client.get('/')

        self.assertEqual(response.code, 200)
        self.assertIn(n1.titulo, response.content)
        self.assertIn(n2.titulo, response.content)
