# -*- coding:utf-8 -*-

from __future__ import absolute_import
# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import MapForm
from .models import Church


def home(request):
    dict_template = {}
    # igrejas = [{'name': 'Templo Central', 'address': 'Brazil, Recife, Avenida Cruz Cabugá 29'}, {'name': 'Campo Grande', 'address': 'Brazil, Recife, Rua Odorico Mendes 327'}, {'name': 'Encruzilhada', 'address': 'Brazil, Recife, Rua Castro Alves 255'}]
    igrejas = Church.objects.all()
    dict_template['igrejas'] = igrejas
    return render_to_response("map.html", dict_template, context_instance=RequestContext(request))


def map_page(request):
    if request.method == 'POST':
        form = MapForm(request.POST)
        print(form)
        if form.is_valid():
            address = "Brazil " + form.cleaned_data['address']

            dict_template = {'address': address}
            igrejas = Church.objects.all()
            dict_template['igrejas'] = igrejas

    else:
        dict_template = {}

    return render_to_response("map.html", dict_template, context_instance=RequestContext(request))
