========================
geo_church
========================

Este site foi construído com o framework web Django (versão 1.6.5) e Python (versão 3.4). A configuração para o desenvolvimento do projeto é bastante simples.

Instalação do Python
====================

Se você estiver em um sistema Linux ou Mac OS X, o Python provavelmente já está instalado. Se não estiver instalado ou
se não estiver usando um desses sistemas, uma busca rápida na internet pode ajudar na instalação do Python.
Ou, se preferir siga as instruções neste link: http://www.pythonize.org/blog/iniciando-programacao-python/

Instalação de virtualenv
========================

Recomendamos utilizar o virtualenv para separar as dependências deste projeto do ambiente python do seu sistema.
Se você estiver em um sistema Linux ou Mac OS X, você pode utilizar o virtualenvwrapper para ajudar a gerenciar
diversos virtualenvs criados para diferentes projetos.

Virtualenv
----------

Após a instalação do virtualenv, crie um ambiente e ative::

    $ virtualenv geo_church
    $ source geo_church/bin/activate

Virtualenv com virtualenvwrapper
------------------------------------

No Linux e Mac OSX, você pode instalar o virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
que gerencia seus ambientes virtuais e adiciona o path do projeto ao `site-directory`.

A instalação é bem simples utilizando o pip::

    $ pip install virtualenvwrapper
    $ export WORKON_HOME=~/Envs
    $ mkdir -p $WORKON_HOME
    $ source /usr/local/bin/virtualenvwrapper.sh

    $ mkvirtualenv geo_church

Para ativar o ambiente basta fazer::

    $ workon geo_church

Usando virtualenvwrapper no Windows
----------------------------------------

Existe uma versão especial do virtualenvwrapper para Windows (https://pypi.python.org/pypi/virtualenvwrapper-win).::

    > mkvirtualenv geo_church

Instalando os pacotes necessários para desenvolvimento
======================================================

Dependendo de onde vocês está instalando as dependências, basta ir até o diretório do projeto aonde está o arquivo
requirements.txt e executar o seguinte (certifique-se que o seu ambiente virtual está ativo):

Em desenvolvimento::

    $ pip install -r requirements/local.txt

Para produção::

    $ pip install -r requirements.txt


Executando o projeto
====================

Com o ambiente virtual ativo, vá até o diretório do projeto Django (local onde está o manage.py) e execute o seguinte comando::

    $ python manage.py runserver

O Django roda na porta 8000 por padrão, então acesse a seguinte url no seu navegador: http://localhost:8000


Follows Best Practices
======================

.. image:: http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png
   :name: Two Scoops Logo
   :align: center
   :alt: Two Scoops of Django
   :target: http://twoscoopspress.org/products/two-scoops-of-django-1-6

This project follows best practices as espoused in `Two Scoops of Django: Best Practices for Django 1.6`_.

.. _`Two Scoops of Django: Best Practices for Django 1.6`: http://twoscoopspress.org/products/two-scoops-of-django-1-6
