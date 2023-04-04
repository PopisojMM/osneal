from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from mascotas.forms import MascotaForm
from mascotas.models import Mascota
from usuarios.models import Usuario
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.


class CrearMAscota(CreateView):
    '''Clase para crear mascotas'''
    template_name = 'mascotas/carga_admin.html'
    success_url = reverse_lazy('mascotas:carga')
    form_class = MascotaForm
    success_url = reverse_lazy('mascotas:index')

    def post(self, request, *args, **kwargs):
        '''Metodo para crear mascotas'''
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            try:
                mascota.duenio = Usuario.objects.get(dni=request.POST.get("dni"))
            except:
                return render(request, self.template_name, {"form": form, "error": "El DNI ingresado no existe"})
            mascota.save()
            return render(request, self.template_name, {'mensaje': 'Mascota creada correctamente'})
        else:
            return render(request, self.template_name, {"form": form})


class BorrarMascota(DeleteView):
    queryset = Mascota.objects.all()
    success_url = reverse_lazy('mascotas:carga')
    template_name = 'mascotas/carga_admin.html'
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        self.delete(self, request, *args, **kwargs)
        return render(request, self.template_name, {"mensaje": "Mascota eliminada correctamente"})


class ModificarMascota(UpdateView):
    '''Clase para modificar mascotas'''
    model = Mascota
    template_name = 'mascotas/modificar.html'
    form_class = MascotaForm
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        context = self.get_context_data()
        context = {'mensaje': 'Mascota modificada correctamente'}
        self.object = form.save()
        return render(self.request, 'mascotas/carga_admin.html', context)
    

class BuscarMascota(ListView):
    '''Clase para buscar mascotas'''
    model = Mascota
    template_name = 'mascotas/resultado_busqueda_mascotas.html'
    context_object_name = 'mascotas'

    def get_queryset(self):
        '''Metodo para buscar mascotas'''
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('mirco_chip',None)
        if busqueda:
            return queryset.filter(micro_chip__contains=busqueda)
        else:
            return queryset
        


def json_buscar_mascota(request, microchip):
    '''Metodo para buscar mascotas por microchip'''
    data = {}
    if request.method == 'GET':
        data = Mascota.objects.filter(
            micro_chip__contains=microchip)[:5].values(
                'id',
                'nombre',
                'micro_chip',
                'especie',
                'raza',
                'pelaje',
                'tipo_plan',
                'duenio__dni',
                'edad',
        )

        if not data:
            return JsonResponse(list(data), safe=False)

        return JsonResponse(list(data), safe=False)
