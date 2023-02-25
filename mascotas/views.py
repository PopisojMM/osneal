from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,UpdateView,CreateView
from .models import Mascota,FormularioMascota
# Create your views here.


class ListadoMascotas(ListView):
    '''
    Lista las mascotas.
    Uso queryset para traer todos los objetos, pero se puede usar el modelo (model=Mascota)
    '''
    queryset = Mascota.objects.all() 
    context_object_name = 'mascotas'
    template_name = 'mascotas/listado.html'

class BorrarMascota(DeleteView):
    '''
    Borra una mascota que se pasa por url el pk.
    Uso queryset para traer todos los objetos, pero se puede usar el modelo (model=Mascota)
    '''
    queryset = Mascota.objects.all()
    success_url = reverse_lazy('mascotas:listado')

class EditarMascota(UpdateView):
    '''
    Edita una mascota que se pasa por url el pk.
    Aca uso el model en lugar del atributo queryset.
    '''
    model = Mascota
    success_url = reverse_lazy('mascotas:listado')
    context_object_name = 'mascota'
    template_name = 'mascotas/editar_mascota.html'
    form_class = FormularioMascota

class CrearMascota(CreateView):
    model = Mascota
    template_name = 'mascotas/crear_mascota.html'
    success_url = reverse_lazy('mascotas:listado')
    form_class = FormularioMascota