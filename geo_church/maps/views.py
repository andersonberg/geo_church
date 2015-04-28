from django.shortcuts import render
from django.shortcuts import render_to_response


def map_page(request):
    dict_template = {}
    if request.method == 'POST':
        dict_template = {'address': 'Brasil, Recife, Rua da Aurora 1035'}

    return render_to_response("map.html", dict_template)
