from django.urls import path
from django.views.generic import TemplateView
from .views import (
    CrearMAscota, 
    json_buscar_mascota,
    BorrarMascota,
    ModificarMascota,
    BuscarMascota,
    )

app_name = 'mascotas'

urlpatterns = [
    path('carga/', CrearMAscota.as_view(),name='carga'),
    path('<int:pk>/borrar/', BorrarMascota.as_view(),name='borrar'),
    path('<int:pk>/modificar/', ModificarMascota.as_view(),name='modificar'),
    path('vacuna/', TemplateView.as_view(template_name='mascotas/vacunas_admin.html'),name='vacuna'),
    path('historial/', TemplateView.as_view(template_name='mascotas/historial_medico_admin.html'),name='historial'),
    path('json_buscar_mascota/<microchip>',json_buscar_mascota,name='json_buscar_mascota'),
    path('buscar/', BuscarMascota.as_view(),name='buscar'),
]
