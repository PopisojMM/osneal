from .models import PerfilUsuario
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    '''Formulario para crear un usuario'''
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class PerfilUsuario(forms.ModelForm):
    '''Formulario para crear un perfil de usuario'''
    class Meta:
        model = PerfilUsuario
        exclude = ('usuario',)