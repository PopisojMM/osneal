from .models import PerfilUsuario
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    '''Formulario para crear un usuario'''
    class Meta:
        model = User
        fields = ( 'email','nombre', 'apellido',)
        


class PerfilUsuarioForm(forms.ModelForm):
    '''Formulario para crear un perfil de usuario'''
    class Meta:
        model = PerfilUsuario
        exclude = ('usuario',"fecha_baja","observaciones")