from django import forms
from mascotas.models import Mascota


class MascotaForm(forms.ModelForm):
    '''Formulario para crear una mascota'''
    class Meta:
        model = Mascota
        fields = '__all__'
        exclude = ('duenio',
                   'fecha_ingreso',
                   'fecha_modificacion',
                   'fecha_baja',
                   'activo')