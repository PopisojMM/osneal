from django.urls import path
from django.views.generic import TemplateView
from .views import CrearMAscota

app_name = 'mascotas'

urlpatterns = [
    path('carga/', CrearMAscota.as_view(),name='carga'),
    path('vacuna/', TemplateView.as_view(template_name='mascotas/vacunas_admin.html'),name='vacuna'),
    path('historial/', TemplateView.as_view(template_name='mascotas/historial_medico_admin.html'),name='historial'),
]
