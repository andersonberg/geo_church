__author__ = 'andersonberg'

from django.db import models
from django import forms


class MapForm(forms.Form):
    address = forms.CharField(max_length=255, required=True)
    church_name = forms.CharField(max_length=255)
