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
                   'date_joined')
        

