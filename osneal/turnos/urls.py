from django.urls import path
from django.views.generic import TemplateView
from .views import (
    crear_turno,
    obtener_turnos,
    borrar_turno,
    )


app_name='turnos'

urlpatterns = [
    path('turnos_admin/', TemplateView.as_view(template_name='turnos/admin/turnos_admin.html'),name='turnos_admin'),
    path('crear_turnos_admin/', crear_turno,name='crear_turnos_admin'),
    path('obtener_turnos_admin/', obtener_turnos,name='obtener_turnos_admin'),
    path('borrar_turnos_admin/', borrar_turno,name='borrar_turnos_admin'),
    path('turnos_usuario/', TemplateView.as_view(template_name='vista_usuarios/turnos_usuario.html'),name='turnos_usuario'),
]
