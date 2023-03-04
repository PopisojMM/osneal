from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .models import Veterinario
from django.urls import reverse_lazy


# Create your views here.
class UserLoginView(LoginView):
    '''Clase para el login de usuarios'''

    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        '''Redirecciona al usuario veterinario a usuarios:alta-propietarios,
        solo si es veterinario, caso contrario redirecciona mascotas:index'''
        if Veterinario.objects.filter(usuario=self.request.user).exists():
            return reverse('usuarios:alta-propietarios')
        else:
            return reverse('mascotas:index')

class UserLogoutView(LoginView):
    '''Clase para el logout de usuarios'''

    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('mascotas:index')
