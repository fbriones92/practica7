# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def consultar(request, persona_id = None):
    template = ''
    datos = {}
    
    if persona_id is None:
        template = 'persona/consultar_personas.html'
    else:
        template = 'persona/consultar_persona.html'
        
    return render(request, template, datos)


def crear(request):
    template = 'persona/crear_persona.html'
    datos = {}
    return render(request, template, datos)

def actualizar(request, persona_id):
    pass

def eliminar(request, persona_id):
    pass