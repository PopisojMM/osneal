from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import UserForm,PerfilUsuarioForm
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model

Usuario = get_user_model()

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

    template_name = 'usuarios/carga_usuarios_admin.html'
    queryset = None

    def get(self, request, *args, **kwargs):
        '''Muestra el formulario para crear usuarios'''
        user_form = UserForm()
        perfil_form = PerfilUsuarioForm()
        return render(request, self.template_name, {'user_form': user_form, 'perfil_form': perfil_form})

    def post(self, request, *args, **kwargs):
        '''Procesa el formulario para crear usuarios'''
        user_form = UserForm(request.POST)
        perfil_form = PerfilUsuarioForm(request.POST, request.FILES)
        print(perfil_form.fields['fecha_nacimiento'])
        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            perfil = perfil_form.save(commit=False)
            perfil.usuario = user
            user.set_password(str(perfil_form.cleaned_data['dni']))
            user.save()
            perfil.save()
            return redirect('usuarios:login')
        else:
            return render(request, self.template_name, {'user_form': user_form, 'perfil_form': perfil_form})


class BuscarUsuarioView(ListView):
    '''Lista los usuarios que coincidan con el criterio de búsqueda'''
    template_name = 'usuarios/resultado_busqueda_usuarios.html'
    model = Usuario
    context_object_name = 'usuarios'

    def get_queryset(self):
        '''Devuelve los usuarios que coincidan con el criterio de búsqueda'''
        queryset = super().get_queryset()
        queryset = queryset.filter(perfilusuario__dni=self.request.GET.get("dni_usuario"))
        return queryset