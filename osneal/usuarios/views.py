from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import UserForm,PerfilUsuarioForm
from django.views.generic import CreateView




# Create your views here.
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


class CrearUsuarioView(CreateView):
    '''Clase para crear usuarios.
    '''

    template_name = 'usuarios/crear_usuario.html'

    def get(self, request, *args, **kwargs):
        '''Muestra el formulario para crear usuarios'''
        user_form = UserForm()
        perfil_form = PerfilUsuarioForm()
        return render(request, self.template_name, {'user_form': user_form, 'perfil_form': perfil_form})

    def post(self, request, *args, **kwargs):
        '''Procesa el formulario para crear usuarios'''
        user_form = UserForm(request.POST)
        perfil_form = PerfilUsuarioForm(request.POST, request.FILES)
        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            perfil = perfil_form.save(commit=False)
            perfil.usuario = user
            user.save()
            perfil.save()
            return redirect('usuarios:login')
        else:
            return render(request, self.template_name, {'user_form': user_form, 'perfil_form': perfil_form})
