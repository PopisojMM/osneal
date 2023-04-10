from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    '''Formulario para crear un usuario'''
    class Meta:
        model = User
        fields = '__all__'
        exclude = ('password',
                   'groups', 
                   'user_permissions', 
                   'last_login',
                   'is_admin',
                   'is_staff',
                   'date_joined',
                   'fecha_baja'
                   )
        
        widgets = {
                        "nombre": forms.TextInput(attrs={'class': 'form-control'}),
                        "apellido": forms.TextInput(attrs={'class': 'form-control'}),
                        "is_active": forms.CheckboxInput(attrs={'class': 'mt-4',}),
                        "email": forms.EmailInput(attrs={'class': 'form-control'}),
                        "groups": forms.SelectMultiple(attrs={'class': 'form-control'}),
                        "dni": forms.TextInput(attrs={'class': 'form-control'}),
                        "telefono": forms.TextInput(attrs={'class': 'form-control'}),
                        "direccion": forms.TextInput(attrs={'class': 'form-control'}),
                        "localidad": forms.TextInput(attrs={'class': 'form-control'}),
                        "provincia": forms.TextInput(attrs={'class': 'form-control'}),
                        "codigo_postal": forms.TextInput(attrs={'class': 'form-control'}),
                        "fecha_nacimiento": forms.DateInput(attrs={
                            'class': 'form-control',
                            'type': 'date',
                            'value': "{{object.fecha_nacimiento}}",
                        },
                            format='%Y-%m-%d',),
                        "fecha_baja": forms.DateInput(attrs={
                            'class': 'form-control',
                            'type': 'date',
                            'value': "{{object.fecha_baja}}",
                        },
                            format='%Y-%m-%d',),
                        "tipo_usuario": forms.Select(attrs={'class': 'form-control'}),
                        "observaciones": forms.Textarea(attrs={'class': 'form-control'}),

                    }

