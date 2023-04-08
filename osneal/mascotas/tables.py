import django_tables2 as tables
from .models import Vacuna


class VacunaTable(tables.Table):
    '''Tabla para mostrar las vacunas'''
    class Meta:
        model = Vacuna
        template_name = 'django_tables2/bootstrap.html'
        fields = ('mascota', 'tipo_vacuna', 'fecha_vacuna', 'fecha_proxima_vacuna', 'nro_vacuna')
        attrs = {"class": "table table-striped table-hover table-responsive",
                 }
