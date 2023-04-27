import django_tables2 as tables
from .models import Vacuna, HistorialClinico



class VacunaTable(tables.Table):
    '''Tabla para mostrar las vacunas'''

    acciones = tables.TemplateColumn(
        '<a class="btn btn-primary" href="{% url "mascotas:editar_vacuna" record.id %}">Editar</a> '
        '<a class="btn btn-danger" data-confirm="¿Estas seguro de eliminar la vacuna de <strong>{{record.mascota.nombre}}</strong>?" href="{% url "mascotas:borrar_vacuna" record.id %}">Eliminar</a>',
        verbose_name='Acciones'
    )

    class Meta:
        model = Vacuna
        template_name = 'django_tables2/bootstrap.html'
        fields = ('mascota', 'tipo_vacuna', 'fecha_vacuna', 'fecha_proxima_vacuna', 'nro_vacuna')
        attrs = {"class": "table table-striped table-hover table-responsive",
                 }

class VacunaTablePropietario(tables.Table):
    '''Tabla para mostrar las vacunas al propietario'''
    class Meta:
        model = Vacuna
        template_name = 'django_tables2/bootstrap.html'
        fields = ('mascota', 'tipo_vacuna', 'fecha_vacuna', 'fecha_proxima_vacuna', 'nro_vacuna')
        attrs = {"class": "table table-striped table-hover table-responsive",
                 }


class HistorialTable(tables.Table):
    '''Tabla para mostrar los historiales clinicos'''
    acciones = tables.TemplateColumn(
        '<a class="btn btn-primary" href="{% url "mascotas:editar_historial" record.id %}">Editar</a> '
        '<a class="btn btn-danger" data-confirm="¿Estas seguro de eliminar el historial de <strong>{{record.mascota.nombre}}</strong>?" href="{% url "mascotas:borrar_historial" record.id %}">Eliminar</a>',
        verbose_name='Acciones'
    )
    class Meta:
        model = HistorialClinico
        template_name = 'django_tables2/bootstrap.html'
        fields = ('mascota', 'fecha_historial', 'diagnostico', 'tratamiento')
        attrs = {"class": "table table-striped table-hover table-responsive",
                 }

class HistorialTablePropietario(tables.Table):
    '''Tabla para mostrar los historiales clinicos'''

    class Meta:
        model = HistorialClinico
        template_name = 'django_tables2/bootstrap.html'
        fields = ('mascota', 'fecha_historial', 'diagnostico', 'tratamiento')
        attrs = {"class": "table table-striped table-hover table-responsive",
                 }

