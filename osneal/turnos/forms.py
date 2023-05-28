from django import forms
from .models import Turno
from mascotas.models import Mascota
from django.utils import timezone


class TurnoForm(forms.ModelForm):

    descripcion = forms.CharField(required=False)

    class Meta:
        model = Turno
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        inicio = self.cleaned_data['inicio']
        fin = self.cleaned_data['fin']

        if inicio > fin:
            raise forms.ValidationError("La fecha de inicio no puede mayor a la fecha de fin.")
        elif fin < inicio:
            raise forms.ValidationError("La fecha de fin no puede ser menor a la fecha de inicio.")

        return cleaned_data
