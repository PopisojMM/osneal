from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.http import JsonResponse
from .models import Perfil
from dal import autocomplete
from .models import User

class InicarSesion(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('mascotas:listado')

class CerrarSesion(LogoutView):
    success_url = reverse_lazy('users:login')

