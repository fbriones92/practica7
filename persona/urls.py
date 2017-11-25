'''
Created on 3 may. 2017

@author: Frank
'''

from django.conf.urls import url
from persona.views import consultar, actualizar, eliminar, crear

urlpatterns = [
    url(r'^$', consultar, name='consultar_personas'),
    url(r'^crear/$', crear, name='crear_persona'),
    url(r'^actualizar/(?P<persona_id>\d+)/$', actualizar, name='actualizar_persona'),
    url(r'^eliminar/(?P<persona_id>\d+)/$', eliminar, name='eliminar_persona'),
    url(r'^consultar/(?P<persona_id>\d+)/$', consultar, name='consultar_persona'),
]