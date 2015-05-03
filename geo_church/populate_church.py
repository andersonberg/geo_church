from __future__ import absolute_import
__author__ = 'andersonberg'

import os
from    maps.models import Church


def populate():
    cidade = "Recife"
    # add_church(name="Templo Central", city=cidade, address="Avenida Cruz Cabugá 29")
    # add_church(name="Encruzilhada", city=cidade, address="Rua Castro Alves 255")
    # add_church(name="Campo da Vovozinha", city=cidade, address="Avenida Doutor Jayme da Fonte 285")
    # add_church(name="Ilha João de Barros", city=cidade, address="Avenida Governador Agamenon Magalhães 100")
    add_church(name="Jerônimo Vilela", city=cidade, address="Avenida Professor José dos Anjos 80")

    for c in Church.objects.all():
        print("- {0}".format(str(c.name)))


def add_church(name, city, address):
    c = Church.objects.get_or_create(name=name, city=city, address=address)[0]
    return c


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geo_church.settings.base')
    populate()
