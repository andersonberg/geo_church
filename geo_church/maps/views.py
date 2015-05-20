# -*- coding:utf-8 -*-

from __future__ import absolute_import
# from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import MapForm, ContatoForm
from .models import Church


def home(request):
    dict_template = {}
    igrejas = Church.objects.all()
    dict_template['igrejas'] = igrejas
    return render_to_response("map.html", dict_template, context_instance=RequestContext(request))


def map_page(request):
    if request.method == 'POST':
        form = MapForm(request.POST)
        if form.is_valid():
            part_address = form.cleaned_data['address']
            address = part_address + ", Brazil"
            # address = address.replace(u"\u2060", "")
            church_name = form.cleaned_data['church_name']

            dict_template = {'address': address}
            igrejas = Church.objects.all()
            dict_template['igrejas'] = igrejas
            dict_template['church'] = church_name
            dict_template['part_address'] = part_address

    else:
        dict_template = {}

    return render_to_response("map.html", dict_template, context_instance=RequestContext(request))


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                "E-mail de Encontre sua igreja - Contato: %s" % email,
                "Mensagem:\n%s" % mensagem,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_TO_EMAIL],
                fail_silently=False
            )

            return HttpResponseRedirect(reverse("contato_ok"))

    else:
        form = ContatoForm()

    dict_template = {
        'form': form,
    }

    return render_to_response("contato.html", dict_template, context_instance=RequestContext(request))

