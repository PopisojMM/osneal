from django import forms
from mascotas.models import Mascota, Vacuna,HistorialClinico


class MascotaForm(forms.ModelForm):
    '''Formulario para crear una mascota'''
    class Meta:
        model = Mascota
        fields = '__all__'
        exclude = ('duenio',
                   'fecha_ingreso',
                   'fecha_modificacion',
                   'fecha_baja',
                   'edad'
                   )
        widgets = {"nombre": forms.TextInput(attrs={'class': 'form-control'}),
                   "micro_chip": forms.TextInput(attrs={'class': 'form-control'}),
                   "especie": forms.TextInput(attrs={'class': 'form-control'}),
                   "raza": forms.TextInput(attrs={'class': 'form-control'}),
                   "pelaje": forms.TextInput(attrs={'class': 'form-control'}),
                   "tipo_plan": forms.Select(attrs={'class': 'form-control'}),
                   "fecha_nacimiento": forms.DateInput(
            attrs={
                'class': 'form-control', 
                'type': 'date',
                'value': "{{object.fecha_nacimiento}}",
            },
            format='%Y-%m-%d',
        ),
        }


class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacuna
        fields = ('tipo_vacuna', 'fecha_vacuna', 'fecha_proxima_vacuna', 'nro_vacuna')
        widgets = {
            'tipo_vacuna': forms.Select(attrs={'class': 'form-control'}),
            'fecha_vacuna': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_proxima_vacuna': forms.DateInput(attrs={'class': 'form-control'}),
            'nro_vacuna': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HistorialForm(forms.ModelForm):
    class Meta:
        model=  HistorialClinico
        fields = '__all__'
        exclude = ('mascota',)