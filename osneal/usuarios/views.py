from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import UserForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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
        return render(request, self.template_name, {'user_form': user_form})

    def post(self, request, *args, **kwargs):
        '''Procesa el formulario para crear usuarios'''
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(str(user_form.cleaned_data['dni']))
            if user_form.cleaned_data['tipo_usuario'] == 'administrador':
                user.is_staff = True
                user.is_admin = True
                user.is_superuser = True
            user.is_active = True
            user.save()
            return render(request,
                          self.template_name,
                          {
                              'user_form': user_form,
                              'mensaje' : 'Usuario creado correctamente'
                            }
                          )
        else:
            return render(request,
                          self.template_name,
                          {
                              'user_form': user_form,
                            }
                          )


class BuscarUsuarioView(ListView):
    '''Lista los usuarios que coincidan con el criterio de búsqueda'''
    template_name = 'usuarios/resultado_busqueda_usuarios.html'
    model = Usuario
    context_object_name = 'usuarios'

    def get_queryset(self):
        '''Devuelve los usuarios que coincidan con el criterio de búsqueda'''
        queryset = super().get_queryset()
        queryset = queryset.filter(dni__contains=self.request.GET.get("dni_usuario"))
        return queryset


class EditarUsuarioView(UpdateView):
    '''Clase para editar usuarios.
    '''
    form_class = UserForm
    template_name = 'usuarios/editar_usuario_admin.html'
    success_url = reverse_lazy('usuarios:crear_usuario')
    queryset = Usuario.objects.all()


class BorrarUsuarioView(DeleteView):
    queryset = Usuario.objects.all()
    success_url = reverse_lazy('usuarios:crear_usuario')
    template_name = 'usuarios/carga_usuarios_admin.html'
    pk_url_kwarg = 'pk'	

    def get(self, request, *args, **kwargs):
        self.delete(self, request, *args, **kwargs)
        return render(request,self.template_name,{"mensaje":"Usuario eliminado correctamente"})