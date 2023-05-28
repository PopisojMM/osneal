from django.urls import path
from django.views.generic import TemplateView
from .views import (
    crear_turno,
    obtener_turnos,
    borrar_turno,
    )


app_name='turnos'

urlpatterns = [

    path('crear_turnos_admin/', crear_turno,name='turnos_admin'),
    path('obtener_turnos_admin/', obtener_turnos,name='obtener_turnos_admin'),
    path('borrar_turnos_admin/', borrar_turno,name='borrar_turnos_admin'),
]
