from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,UpdateView
from .models import Mascota,FormularioMascota
# Create your views here.


class ListadoMascotas(ListView):
    queryset = Mascota.objects.all()
    context_object_name = 'mascotas'
    template_name = 'mascotas/listado.html'

class BorrarMascota(DeleteView):
    queryset = Mascota.objects.all()
    success_url = reverse_lazy('mascotas:listado')

class EditarMascota(UpdateView):
    model = Mascota
    success_url = reverse_lazy('mascotas:listado')
    context_object_name = 'mascota'
    template_name = 'mascotas/editar_mascota.html'
    form_class = FormularioMascota