from django.contrib import admin
from django.urls import path
from .views import InicarSesion,CerrarSesion,buscar_usuario

app_name = 'users'

urlpatterns = [
    path('iniciar-sesion/',InicarSesion.as_view(),name='iniciar-sesion'),
    path('salir/',CerrarSesion.as_view(),name='salir'),
]
