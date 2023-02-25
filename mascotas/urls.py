from django.urls import path
from .views import ListadoMascotas,BorrarMascota,EditarMascota

app_name = 'mascotas'

urlpatterns = [
    path('listado/',ListadoMascotas.as_view(),name='listado'),
    path('<int:pk>/borrar/',BorrarMascota.as_view(),name='borrar'),
    path('<int:pk>/editar/',EditarMascota.as_view(),name='editar'),
]
