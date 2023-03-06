from .models import Propietario, Veterinario
from django import forms

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = [
            'usuario', 
            'dni', 
            'telefono', 
            'email', 
            'direccion', 
            'localidad', 
            'provincia', 
            'codigo_postal', 
            'fecha_nacimiento', 
            'observaciones'
            ]
