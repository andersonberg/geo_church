__author__ = 'andersonberg'

from django.db import models
from django import forms


class MapForm(forms.Form):
    address = forms.CharField(max_length=255, required=True)
    church_name = forms.CharField(max_length=255)


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    mensagem = forms.CharField(required=True, widget=forms.Textarea())