from django.http import HttpResponse
from django.template import Template
from django.template.loader import get_template


def index(request):
    
    carga_index=get_template('index-onepage.html')

    index_cargado=carga_index.render()

    return HttpResponse(index_cargado)