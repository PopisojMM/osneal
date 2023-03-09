from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import PerfilUsuario
from .forms import UserForm




# Create your views here.
class UserLoginView(LoginView):
    '''Clase para el login de usuarios'''

    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        '''Redirecciona al usuario veterinario a usuarios:alta-usuarios,
        solo si es veterinario, caso contrario redirecciona mascotas:index'''
        if PerfilUsuario.objects.filter(usuario=self.request.user).exists():
            return reverse('usuarios:crear-usuarios')
        else:
            return reverse('mascotas:index')

class UserLogoutView(LoginView):
    '''Clase para el logout de usuarios'''

    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('mascotas:index')



