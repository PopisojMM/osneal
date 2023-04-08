from django.urls import path,re_path
from django.views.generic import TemplateView
from .views import (
    CrearMascota, 
    json_buscar_mascota,
    BorrarMascota,
    ModificarMascota,
    BuscarMascota,
    CrearHistorial,
    CrearVacunaView,
    MascotasAutocomplete,
    ListarVacunasView,
    EditarVacunaView,
    BorrarVacunaView,
    
    )

app_name = 'mascotas'

urlpatterns = [
    path('carga/', CrearMascota.as_view(),name='carga'),
    path('<int:pk>/borrar/', BorrarMascota.as_view(),name='borrar'),
    path('<int:pk>/modificar/', ModificarMascota.as_view(),name='modificar'),
    path('historial/', TemplateView.as_view(template_name='mascotas/historial_medico_admin.html'),name='historial'),
    path('carga_historial/', CrearHistorial.as_view(),name='carga_historial'),
    path('json_buscar_mascota/<microchip>',json_buscar_mascota,name='json_buscar_mascota'),
    path('buscar/', BuscarMascota.as_view(),name='buscar'),
    path('carga_vacuna/', CrearVacunaView.as_view(),name='carga_vacuna'),
    re_path(
        r'^mascotas-autocomplete/$',
        MascotasAutocomplete.as_view(),
        name='mascotas-autocomplete',
    ),
    path('<int:pk>/listado_vacunas/', ListarVacunasView.as_view(),name='listado_vacunas'),
    path('<int:pk>/editar_vacuna/', EditarVacunaView.as_view(),name='editar_vacuna'),
    path('<int:pk>/borrar_vacuna/', BorrarVacunaView.as_view(),name='borrar_vacuna'),
    ]
