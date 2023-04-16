from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import UserForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from dal import autocomplete
from django.contrib import messages




Usuario = get_user_model()
class UsuarioAutocomplete(PermissionRequiredMixin,autocomplete.Select2QuerySetView):
    '''Clase para autocompletar mascotas'''
    permission_required = 'usuarios.add_usuario'
    login_url = reverse_lazy('usuarios:login')

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Usuario.objects.none()

        qs = Usuario.objects.all().exclude(is_staff=True)

        if self.q:
            qs = qs.filter(dni__istartswith=self.q)

        return qs

# Usuarios

class UserLoginView(LoginView):
    '''Clase para el login de usuarios'''

    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('usuarios:crear_usuario')

    def get(self, request, *args, **kwargs):
        '''Muestra el formulario de login'''
        if request.user.is_authenticated and not request.user.is_staff:
            self.next_page = reverse_lazy('mascotas:index')

        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        '''Redirecciona al usuario veterinario a usuarios:alta-usuarios,
        solo si es veterinario, caso contrario redirecciona mascotas:index'''
        if self.request.user.is_staff:
            return reverse('usuarios:crear_usuario')
        else:
            return reverse('mascotas:index')


class UserLogoutView(LogoutView):
    '''Clase para el logout de usuarios'''

    template_name = 'usuarios/login.html'
    next_page = reverse_lazy('usuarios:login')


class CrearUsuarioView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    '''Clase para crear usuarios.
    '''

    template_name = 'usuarios/carga_usuarios_admin.html'
    model = Usuario
    form_class = UserForm
    success_url = reverse_lazy('usuarios:crear_usuario')
    success_message = "Usuario creado correctamente"
    permission_required = 'usuarios.add_usuario'
    login_url = reverse_lazy('usuarios:login')
    


class EditarUsuarioView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    '''Clase para editar usuarios.
    '''
    form_class = UserForm
    template_name = 'usuarios/editar_usuario_admin.html'
    queryset = Usuario.objects.all()
    success_url = reverse_lazy('usuarios:crear_usuario')
    success_message = "Usuario editado correctamente"
    permission_required = 'usuarios.change_usuario'
    login_url = reverse_lazy('usuarios:login')

    def get_queryset(self, *args, **kwargs):
        '''Solo los usuarios admin pueden editar usuarios admin'''
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.exclude(is_staff=True)




class BorrarUsuarioView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    queryset = Usuario.objects.all()
    success_url = reverse_lazy('usuarios:crear_usuario')
    template_name = 'usuarios/asd.html'
    pk_url_kwarg = 'pk'
    permission_required = 'usuarios.delete_usuario'
    login_url = reverse_lazy('usuarios:login')
    success_message = 'Usuario eliminado correctamente'

    def get(self, request, *args, **kwargs):
        self.delete(self, request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, self.success_message)
        return redirect(self.success_url)
    

def json_buscar_usuario(request,dni):
    '''Retorna usuarios que coincidan con el criterio de búsqueda'''
    data = {}
    if request.method == 'GET' and dni: 
        #limitar luego a que solo usuarios admin puedan acceder aca
    
        data = Usuario.objects.filter(
            dni__contains=dni).values('id','dni','nombre','apellido')


    return JsonResponse(list(data),safe=False)

class BuscarUsuarioView(PermissionRequiredMixin,ListView):
    '''Lista los usuarios que coincidan con el criterio de búsqueda'''
    template_name = 'usuarios/resultado_busqueda_usuarios.html'
    model = Usuario
    context_object_name = 'usuarios'
    permission_required = 'usuarios.view_usuario'

    def get_queryset(self, *args, **kwargs):
        '''Devuelve los usuarios que coincidan con el criterio de búsqueda'''
        queryset = super().get_queryset()
        usuario_buscado = self.request.GET.get("dni_usuario",None)
        if usuario_buscado:
            queryset = queryset.filter(dni__contains=usuario_buscado)
        
        if self.request.user.is_staff:
            return queryset
        else:
            return queryset.exclude(is_staff=True)
    

# TURNOS
