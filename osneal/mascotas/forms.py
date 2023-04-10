from django import forms
from mascotas.models import Mascota, Vacuna, HistorialClinico
from dal import autocomplete
from django.urls import reverse_lazy


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
        fields = '__all__'
        widgets = {
            'mascota':  autocomplete.ModelSelect2(url=reverse_lazy('mascotas:mascotas-autocomplete')),
            'tipo_vacuna': forms.Select(attrs={'class': 'form-control'}),
            'fecha_vacuna': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'value': "{{object.fecha_nacimiento}}",
            },
                format='%Y-%m-%d',),
            'fecha_proxima_vacuna': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'value': "{{object.fecha_nacimiento}}",
            },
                format='%Y-%m-%d',),
            'nro_vacuna': forms.TextInput(attrs={'class': 'form-control'}),
        }


class HistorialForm(forms.ModelForm):
    class Meta:
        model = HistorialClinico
        fields = '__all__'

        widgets = {
            'mascota':  autocomplete.ModelSelect2(url=reverse_lazy('mascotas:mascotas-autocomplete')),
            'fecha_historial': forms.DateInput(attrs={
                'class': 'form-control w-50',
                'type': 'date',
                'value': "{{object.fecha_nacimiento}}",
            },
                format='%Y-%m-%d',),
                'diagnostico': forms.TextInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
        }