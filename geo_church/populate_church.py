# -*- encoding:utf-8 -*-

from __future__ import absolute_import
__author__ = 'andersonberg'

import os
from maps.models import Church


def populate():

    # Área 01
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
    add_church(name="Benfica", city=cidade, address="Rua Clara Basbaum")
    add_church(name="Jerônimo Vilela 2", city=cidade, address="Avenida Professor José dos Anjos 158")
    add_church(name="Sete de Setembro", city=cidade, address="Rua Sete de Setembro 329")
    add_church(name="Rua dos Casados", city=cidade, address="Rua dos Casados 274")
    add_church(name="Beira Rio (Coelhos)", city=cidade, address="Rua Compositor Vinícius de Morais 272")
    add_church(name="Rua do Ocidente", city=cidade, address="RUA DO OCIDENTE 200")
    add_church(name="Rua Timbira - Santo Amaro", city=cidade, address="RUA TIMBIRAS")
    add_church(name="CAMPO GRANDE 2", city=cidade, address="RUA GONCALVES DIAS 538")
    add_church(name="PRAÇA DO DIÁRIO DE PERNAMBUCO", city=cidade, address="RUA LARGA DO ROSARIO 222")

    # Área 02
    cidade = "Recife"
    add_church(name="FUNDÃO", city=cidade, address="AVENIDA BEBERIBE 2980")
    add_church(name="ALTO DOS COQUEIROS", city=cidade, address="RUA LAJE GRANDE 32")
    add_church(name="CAMPOS NOVOS", city=cidade, address="RUA TAGUATINGA")
    add_church(name="CHÃO DE ESTRELAS", city=cidade, address="RUA DOUTOR ELIAS GOMES 74")
    add_church(name="ALTO DEODATO", city=cidade, address="RUA ALTO DO DEODATO 520")
    add_church(name="PRAÇA DA CONVENÇÃO", city=cidade, address="AVENIDA BEBERIBE 4669")
    add_church(name="PORTO DA MADEIRA", city=cidade, address="RUA MARAJO 131")
    add_church(name="ALTO DEODATO 2", city=cidade, address="AVENIDA ANIBAL BENEVOLO 1338")
    add_church(name="VALE DO MONTE", city=cidade, address="RUA VALE DO MONTE 10")
    add_church(name="MANOEL BRAZÃO", city=cidade, address="RUA MANOEL BRAZAO 105")
    add_church(name="BELO HORIZONTE", city=cidade, address="RUA BELO HORIZONTE 147")
    add_church(name="ALTO DO CÉU", city=cidade, address="RUA CONSELHEIRO BARROS BARRETO 526")
    add_church(name="SANTA MERCEDES", city=cidade, address="RUA SANTA MERCEDES 168")
    add_church(name="BATAGUAÇÚ", city=cidade, address="RUA BATAGUACU 43")
    add_church(name="RES.IRMÃO JOSÉ SEVERINO", city=cidade, address="AVENIDA NOVA DO FUNDAO 63")
    add_church(name="RES.DO IRMÃO CARLOS", city=cidade, address="RUA MANOEL SILVA 184")
    add_church(name="RUA DO ANIL", city=cidade, address="RUA DO ANIL 872")
    add_church(name="J. SEVERINO", city=cidade, address="RUA MARCILIO DIAS 14")
    add_church(name="RES.IRMÃO FERNANDO", city=cidade, address="RUA MANOEL BRANDAO 15")
    add_church(name="REGENERAÇÃO", city=cidade, address="RUA HERCULANDIA 125")
    add_church(name="BEIRA RIO BEBERIBE", city=cidade, address="RUA COMPOSITOR VINICIUS DE MORAIS 272")
    add_church(name="TERMINAL CHÃO DE ESTRELAS", city=cidade, address="RUA HONORIO DE SOUZA 14")
    add_church(name="AVENIDA ANÍBAL BENÉVOLO", city=cidade, address="AVENIDA ANÍBAL BENÉVOLO 195")


    # Área 03
    cidade = "Olinda"
    add_church(name="ESTRADA DA MIRUEIRA", city=cidade, address="ESTRADA DA MIRUEIRA 619")
    add_church(name="ALTO DA CONQUISTA 4", city=cidade, address="RUA CICERO RUFINO MARQUES")
    add_church(name="ALTO DA CONQUISTA 2", city=cidade, address="TRAVESSA PORTUGUESA")
    add_church(name="ALTO DA CONQUISTA 1", city=cidade, address="RUA TIJUCA 577")
    add_church(name="ALTO DO SOL NASCENTE", city=cidade, address="RUA DOS DESEJOS 60")
    add_church(name="ALTO DA CONCEIÇÃO", city=cidade, address="RUA LIMA 691")
    add_church(name="ALTO DO SOL NASCENTE 2", city=cidade, address="RUA BATALHA 660")
    add_church(name="ALTO DA CONQUISTA 5", city=cidade, address="RUA DA EDUCACAO")
    add_church(name="ALTO DA CONQUISTA 6", city=cidade, address="RUA MONARCA 15")
    add_church(name="CÓRREGO DO ABACATE", city=cidade, address="Rua Córrego do Abacate 160")
    # add_church(name="RESIDÊNCIA DO IRMÃO CABRAL", city=cidade, address="RUA ASTECA 1")
    # add_church(name="RESIDÊNCIA DO IRMÃO JURANDIR", city=cidade, address="RUA QUADRANTE 93")


    # Área 04
    cidade = "Olinda"
    add_church(name="BULTRINS", city=cidade, address="AVENIDA DOS BULTRINS 80")
    add_church(name="ALTO DA MINA", city=cidade, address="RUA LAJEDO 107")
    add_church(name="OURO PRETO", city=cidade, address="RUA CARNAUBA 19")
    add_church(name="SÍTIO DA UVA", city=cidade, address="RUA PROJETADA 92")
    add_church(name="SÍTIO DA UVA 2", city=cidade, address="AVENIDA PERIMETRAL NORTE")
    add_church(name="JATOBÁ", city=cidade, address="RUA JOAO FIGUEIREDO MAIA 191")
    add_church(name="JATOBÁ 1", city=cidade, address="RUA DOUTOR ANTONIO JOSE DE ALMEIDA PERNAMBUCO 103")
    add_church(name="JARDIM BRASIL", city=cidade, address="RUA FORTALEZA 15")
    add_church(name="PARQUE VENCEDOR 2", city=cidade, address="RUA GUAIANAZES 33")
    add_church(name="BAIXA DA MINA", city=cidade, address="RUA AVENCA 139")
    add_church(name="BAIXA DA MINA 2", city=cidade, address="RUA SAO CAETANO 209")
    add_church(name="PARQUE VENCEDOR", city=cidade, address="RUA ALGODOEIRO")
    add_church(name="ARGENTINA", city=cidade, address="RUA JOSE DE OLIVEIRA E SILVA 286")
    add_church(name="PE-15 - ARGENTINA", city=cidade, address="AVENIDA DOUTOR JOAQUIM NABUCO 2603")
    add_church(name="GOLFINHO DE MELO", city=cidade, address="RUA GOLFINHO")
    add_church(name="QUATRO DE OUTUBRO 2", city=cidade, address="RUA MANOEL FERREIRA 173")
    add_church(name="OURO PRETO-CENTRO", city=cidade, address="RUA CAMOMILA 03")
    add_church(name="SÍTIO DA UVA 3", city=cidade, address="AVENIDA COSTA AZEVEDO 96")
    add_church(name="QUATRO DE OUTUBRO 3", city=cidade, address="RUA SENADOR BARROS DE CARVALHO 171")
    add_church(name="PARQUE VENCEDOR 3", city=cidade, address="Rua Clementino de Carvalho Mendes 158")
    add_church(name="VILA DO SARGENTO-OURO PRETO", city=cidade, address="Rua Atlântico 33")
    add_church(name="RUA COQUEIRAL", city=cidade, address="Rua Coqueiral 130")
    add_church(name="RUA PARÁ", city=cidade, address="RUA PARÁ 501")
    add_church(name="VILA MANCHETE", city=cidade, address="Rua Vinicuius de Morais 16")
    add_church(name="OURO PRETO CENTRO TERMINAL", city=cidade, address="Rua Atlântica 23")
    add_church(name="RUA DO GOLFINHO DE MELO", city=cidade, address="Rua do Golfinho de Melo 14")
    add_church(name="BULTRINS 2", city=cidade, address="RUA MARIA JOSÉ DE ALBUQUERQUE 84")

    # Área 05
    cidade = "Recife"
    add_church(name="CÓRREGO DO EUCLIDES", city=cidade, address="RUA CORREGO DO EUCLIDES 521")
    add_church(name="ALTO JOSÉ DO PINHO", city=cidade, address="RUA HORACIO SILVA 314")
    add_church(name="ALTO DA SAUDADE", city=cidade, address="RUA ALTO DA SERRINHA 4000")
    add_church(name="ALTO DO BRASIL", city=cidade, address="RUA ALTO BRASIL 468")
    add_church(name="MANGABEIRA", city=cidade, address="RUA MARIA GONCALVES 51")
    add_church(name="MORRO DA CONCEIÇÃO", city=cidade, address="RUA NOSSA SENHORA DA CONCEICAO 284")
    add_church(name="CÓRREGO DO TIRO 2", city=cidade, address="RUA ARLINDO CISNEIROS 234")
    add_church(name="CÓRREGO JOSÉ GRANDE", city=cidade, address="RUA CORREGO JOSE GRANDE 249")
    add_church(name="RUA LUCÉLIA", city=cidade, address="RUA LUCÉLIA")
    add_church(name="SÃO DOMINGOS SÁVIO", city=cidade, address="RUA AMANDA 249")
    add_church(name="LADEIRA DO BONIFÁCIO", city=cidade, address="Rua Alto José do Bonifácio")
    add_church(name="Rua do Rio", city=cidade, address="Rua do Rio 523")
    add_church(name="RUA ALTEROSA", city=cidade, address="RUA ALTEROSA")
    add_church(name="LADEIRA SÃO JERÔNIMO", city=cidade, address="Rua dos Calçados 227")
    add_church(name="RUA HIDROLÂNDIA", city=cidade, address="RUA HIDROLÂNDIA 30")
    add_church(name="PLANALTINA", city=cidade, address="RUA PLANALTINA 129")
    add_church(name="EXPANÇÃO ALTO JOSÉ DO PINHO", city=cidade, address="CORREGO DO BARTOLOMEU 392")
    add_church(name="2ª TRAVESSA BELA VISTA", city=cidade, address="TRAVESSA BELA VISTA 75")
    add_church(name="EXPANSÃO ALTO DA SAUDADE", city=cidade, address="RUA ALTO PARAGUAI 7")
    add_church(name="MONTE SANTO", city=cidade, address="RUA MONTE SANTO 481")
    add_church(name="RUA DA VITÓRIA", city=cidade, address="RUA UNIAO DA VITORIA 144")
    add_church(name="RUA DO CHAFARIZ", city=cidade, address="RUA DO CHAFARIZ 164")


    # Área 06
    # cidade = "Olinda"
    # add_church(name="", city=cidade, address="")

    # Área 07
    cidade = "Recife"
    # add_church(name="", city=cidade, address="")
    # add_church(name="", city=cidade, address="")
    # add_church(name="", city=cidade, address="")
    # add_church(name="", city=cidade, address="")
    # add_church(name="", city=cidade, address="")
    # add_church(name="", city=cidade, address="")

    # Área 08
    # cidade = "Recife"

    # Área 09
    # cidade = "Recife"

    # Área 10
    # cidade = "Recife"

    # Área 11
    # cidade = "Recife"

    # Área 12 (Recife/Jaboatão)
    # cidade = "Recife"

    # Área 13 (Recife/Jaboatão)
    # cidade = "Recife"

    # Área 14
    # cidade = "Jaboatão dos Guararapes"

    # Área 15 (Recife/Jaboatão)
    # cidade = "Jaboatão dos Guararapes"

    # Área 16 (Olinda/Recife)
    # cidade = "Olinda"

    # Área 17 (Camaragibe/Recife)
    # cidade = "Camaragibe"

    # Área 18
    # cidade = "Recife"

    # Área 19
    # cidade = "Olinda"

    # Área 20
    # cidade = "Olinda"

    # Área 21
    # cidade = "Recife"

    # Área 22
    # cidade = "Recife"

    # Área 23
    # cidade = "Recife"

    # Área 24 (Recife/Camaragibe)
    # cidade = "Recife"

    # Área 25
    # cidade = "Camaragibe"

    # Área 26
    # cidade = "Olinda"

    # Área 27 (Recife/Olinda)
    # cidade = "Recife"

    # Área 28
    # cidade = "Olinda"

    # Área 29
    # cidade = "Recife"

    # Área 30
    # cidade = "Recife"

    # Área 31
    # cidade = "Recife"

    # Área 32 (Jaboatão/Recife)
    # cidade = "Recife"

    # Área 33
    # cidade = "Jaboatão dos Guararapes"

    # Área 34
    # cidade = "Jaboatão dos Guararapes"

    # Área 35
    # cidade = "Jaboatão dos Guararapes"

    # Área 36
    # cidade = "Jaboatão dos Guararapes"

    # Área 37
    # cidade = "Jaboatão dos Guararapes"

    # Área 38
    # cidade = "Recife"

    # Área 39
    # cidade = "Jaboatão dos Guararapes"

    # Área 40
    # cidade = "Recife"

    # Área 41
    # cidade = "Jaboatão dos Guararapes"

    # Área 42 (Recife/Camaragibe)
    # cidade = "Recife"

    # Área 43
    # cidade = "Recife"

    # Área 44
    # cidade = "Recife"

    # Área 45 (Recife/Jaboatão)
    # cidade = "Jaboatão dos Guararapes"

    # Área 46 (Recife/Jaboatão)
    # cidade = "Jaboatão dos Guararapes"

    # Área 47
    # cidade = "Recife"

    # Área 48 (Recife/Camaragibe)
    # cidade = "Recife"

    # Área 49
    # cidade = "Paulista"

    # Área 50 (Paulista/Itamaracá/Igarassú/Abreu e Lima/Itapissuma)
    # cidade = "Paulista"

    # Área 51 (Camaragibe/São Lourenço)
    # cidade = "Camaragibe"

    # Área 52 (Jaboatão/Cabo)
    # cidade = "Jaboatão dos Guararapes"

    # Área 53 (Cabo/Ponte dos Carvalhos)
    # cidade = "Jaboatão dos Guararapes"

    # Área 54
    # cidade = "Recife"

    # Área 55
    # cidade = "Recife"

    # Área 56 (Recife/Jaboatão)
    # cidade = "Recife"

    # Área 57
    # cidade = "Olinda"


    for c in Church.objects.all():
        print("- {0}".format(str(c.name)))


def add_church(name, city, address):
    c = Church.objects.get_or_create(name=name, city=city, address=address)[0]
    return c


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geo_church.settings.base')
    populate()
