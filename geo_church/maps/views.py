from django.shortcuts import render
from django.shortcuts import render_to_response


def map_page(request):
    dict_template = {}
    return render_to_response("map.html", dict_template)
