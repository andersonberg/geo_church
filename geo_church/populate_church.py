from __future__ import absolute_import
__author__ = 'andersonberg'

import os
from maps.models import Church


def populate():
    cidade = "Recife"
    add_church(name="Templo Central", city=cidade, address="Avenida Cruz Cabugá 29")
    add_church(name="Campo da Vovozinha", city=cidade, address="Avenida Doutor Jayme da Fonte 285")
    add_church(name="Campo Grande", city=cidade, address="Rua Odorico Mendes 327")
    # add_church(name="Coelhos", city=cidade, address="")
    add_church(name="Encruzilhada", city=cidade, address="Rua Castro Alves 255")
    add_church(name="Ilha de Joaneiro", city=cidade, address="Terceira Travessa A 402")
    add_church(name="Ilha João de Barros", city=cidade, address="Avenida Governador Agamenon Magalhães 100")
    add_church(name="Jerônimo Vilela", city=cidade, address="Avenida Professor José dos Anjos 80")
    add_church(name="Vila dos Casados", city=cidade, address="Rua Mário Albuquerque Cavalcante")
    # add_church(name="Benfica", city=cidade, address="")
    add_church(name="Jerônimo Vilela 2", city=cidade, address="Avenida Professor José dos Anjos 158")
    add_church(name="Sete de Setembro", city=cidade, address="Rua Sete de Setembro 329")
    add_church(name="Rua dos Casados", city=cidade, address="Rua dos Casados 274")
    add_church(name="Beira Rio (Coelhos)", city=cidade, address="Rua Compositor Vinícius de Morais 272")
    add_church(name="Rua do Ocidente", city=cidade, address="RUA DO OCIDENTE 200")
    add_church(name="Rua Timbira - Santo Amaro", city=cidade, address="RUA TIMBIRAS")
    add_church(name="CAMPO GRANDE 2", city=cidade, address="RUA GONCALVES DIAS 538")
    add_church(name="PRAÇA DO DIÁRIO DE PERNAMBUCO", city=cidade, address="RUA LARGA DO ROSARIO 222")
    add_church(name="FUNDÃO", city=cidade, address="AVENIDA BEBERIBE 2980")
    add_church(name="ALTO DOS COQUEIROS", city=cidade, address="RUA LAJE GRANDE 32")
    add_church(name="CAMPOS NOVOS", city=cidade, address="RUA TAGUATINGA")
    # add_church(name="", city=cidade, address="")
    # add_church(name="", city=cidade, address="")

    for c in Church.objects.all():
        print("- {0}".format(str(c.name)))


def add_church(name, city, address):
    c = Church.objects.get_or_create(name=name, city=city, address=address)[0]
    return c


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geo_church.settings.base')
    populate()
