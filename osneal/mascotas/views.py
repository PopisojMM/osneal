from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from mascotas.forms import MascotaForm,HistorialForm,VacunaForm
from mascotas.models import Mascota,Vacuna,HistorialClinico
from mascotas.tables import VacunaTable, HistorialTable
from usuarios.models import Usuario
from django.urls import reverse_lazy
from dal import autocomplete
from django_tables2 import SingleTableView
from django.contrib.messages.views import SuccessMessageMixin





# Create your views here.

# MASCOTAS 
class CrearMascota(SuccessMessageMixin,CreateView):
    '''Clase para crear mascotas'''
    template_name = 'mascotas/carga_admin.html'
    success_url = reverse_lazy('mascotas:carga')
    form_class = MascotaForm
    success_url = reverse_lazy('mascotas:carga')
    success_message = "Mascota creada correctamente"



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
        


class MascotasAutocomplete(autocomplete.Select2QuerySetView):
    '''Clase para autocompletar mascotas'''
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Mascota.objects.none()

        qs = Mascota.objects.all()

        if self.q:
            qs = qs.filter(micro_chip__istartswith=self.q)

        return qs

# HISTORIAL

class CrearHistorial(SuccessMessageMixin,CreateView):
    '''Clase para crear historiales'''
    template_name = 'mascotas/historial_medico_admin.html'
    success_url = reverse_lazy('mascotas:carga_historial')
    form_class = HistorialForm

class BorrarHistorial(SuccessMessageMixin,DeleteView):
    '''Clase para eliminar historiales'''
    model = Mascota
    pk_url_kwarg = 'pk'
    success_message = "Historial eliminado correctamente"
    template_name = 'mascotas/carga_admin.html'

    def get(self, request, *args, **kwargs):
        self.delete(self, request, *args, **kwargs)
        return render(request, self.template_name,)
    

class EditarHistorialView(SuccessMessageMixin,UpdateView):
    '''Clase para modificar historiales'''
    model = Mascota
    template_name = 'mascotas/historial_medico_admin.html'
    form_class = HistorialForm
    pk_url_kwarg = 'pk'
    success_message = "Historial modificado correctamente"

class ListarHistorialesView(SingleTableView):
    '''Clase para listar historiales de una mascota'''
    model = HistorialClinico
    template_name = 'mascotas/listado_historiales.html'
    table_class = HistorialTable
 



# VACUNAS
class CrearVacunaView(CreateView):
    '''Clase para crear vacunas'''
    template_name = 'mascotas/vacunas_admin.html'
    success_url = reverse_lazy('mascotas:carga')
    form_class = VacunaForm


class ListarVacunasView(SingleTableView):
    '''Clase para listar vacunas de una mascota'''
    model = Vacuna
    template_name = 'mascotas/listado_vacunas.html'
    context_object_name = 'vacunas'
    table_class = VacunaTable

    def get_queryset(self):
        '''Metodo para buscar mascotas'''
        queryset = super().get_queryset()
        busqueda = self.kwargs.get('pk')
        print(busqueda)
        if busqueda:
            return queryset.filter(mascota=busqueda)
        else:
            return queryset
        

class EditarVacunaView(UpdateView):
    '''Clase para listar vacunas de una mascota'''
    model = Vacuna
    template_name = 'mascotas/vacunas_admin.html'
    form_class = VacunaForm
    pk_url_kwarg = 'pk'


class BorrarVacunaView(SuccessMessageMixin,DeleteView):
    '''Clase para eliminar vacunas de una mascota'''
    model = Vacuna
    pk_url_kwarg = 'pk'
    success_message = "Vacuna eliminada correctamente"
    template_name = 'mascotas/vacunas_admin.html'