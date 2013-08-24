# coding: utf-8
from django.test import TestCase


class SimpleTest(TestCase):
    def test_la_matematica_no_se_rompio(self):
        self.assertEqual(1 + 1, 2)


class AlsoSimpleTest(TestCase):
    fixtures = ['noticias.json']

    def test_inicio_tiene_todas_las_noticias(self):
        n1 = Noticia.objects.get(pk=1)
        n2 = Noticia.objects.get(pk=2)

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(n1.titulo, response.content)
        self.assertIn(n2.titulo, response.content)
