from django.urls import path,re_path
from django.views.generic import TemplateView
from .views import (
    CrearMascota,
    BorrarMascota,
    ModificarMascota,
    BuscarMascota,
    CrearHistorial,
    EditarHistorialView,
    ListarHistorialesView,
    BorrarHistorialVew,
    CrearVacunaView,
    MascotasAutocomplete,
    MascotasByDniAutocomplete,
    ListarVacunasView,
    EditarVacunaView,
    BorrarVacunaView,

    #Vistas para usuarios propietarios
    MisMascotasView,
    VacunasMisMascotasView,
    HistorialesMisMascotasView,

    )

app_name = 'mascotas'

urlpatterns = [
    # MASCOTAS ADMIN
    path('carga/', CrearMascota.as_view(),name='carga'),
    path('<int:pk>/borrar/', BorrarMascota.as_view(),name='borrar'),
    path('<int:pk>/modificar/', ModificarMascota.as_view(),name='modificar'),
    path('buscar/', BuscarMascota.as_view(),name='buscar'),

    # HISTORIALES ADMIN
    path('carga_historial/', CrearHistorial.as_view(),name='carga_historial'),
    path('<int:pk>/editar_historial/', EditarHistorialView.as_view(),name='editar_historial'),
    path('<int:pk>/listado_historiales/', ListarHistorialesView.as_view(),name='listado_historiales'),
    path('<int:pk>/borrar_historial/', BorrarHistorialVew.as_view(),name='borrar_historial'),

    # VACUNAS ADMIN
    path('carga_vacuna/', CrearVacunaView.as_view(),name='carga_vacuna'),
    path('<int:pk>/listado_vacunas/', ListarVacunasView.as_view(),name='listado_vacunas'),
    path('<int:pk>/editar_vacuna/', EditarVacunaView.as_view(),name='editar_vacuna'),
    path('<int:pk>/borrar_vacuna/', BorrarVacunaView.as_view(),name='borrar_vacuna'),

    #URLS PARA USUARIOS COMUNES
    path('mis_mascotas/',MisMascotasView.as_view(),name='mis_mascotas'),
    path('mis_mascotas/vacunas',VacunasMisMascotasView.as_view(),name='mis_mascotas_vacunas'),
    path('mis_mascotas/historial',HistorialesMisMascotasView.as_view(),name='mis_mascotas_historial'),

    # AUTOCOMPLETE
    re_path(
        r'^mascotas-autocomplete/$',
        MascotasAutocomplete.as_view(),
        name='mascotas-autocomplete',
    ),
    re_path(
        r'^mascotas-by-dni-autocomplete/$',
        MascotasByDniAutocomplete.as_view(),
        name='mascotas-by-dni-autocomplete',
    ),

    ]
