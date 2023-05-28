from django.urls import path
from django.views.generic import TemplateView
from .views import (
    crear_turno,
    )


app_name='turnos'

urlpatterns = [

    path('crear_turnos_admin/', crear_turno,name='turnos_admin'),
]
