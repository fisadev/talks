# coding: utf-8
from django import forms

from sitio.models import Comentario


class ContactoForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    texto = forms.CharField(widget=forms.Textarea)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        exclude = ('noticia', )
