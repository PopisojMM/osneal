from django.shortcuts import render,redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from mascotas.forms import MascotaForm,HistorialForm,VacunaForm, EditarHistorialForm,EditarVacunaForm
from mascotas.models import Mascota,Vacuna,HistorialClinico
from usuarios.models import Usuario
from mascotas.tables import VacunaTable, HistorialTable,VacunaTablePropietario,HistorialTablePropietario
from django.urls import reverse_lazy
from dal import autocomplete
from django_tables2 import SingleTableView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages




# MASCOTAS
class CrearMascota(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    '''Clase para crear mascotas'''
    template_name = 'mascotas/carga_admin.html'
    success_url = reverse_lazy('mascotas:carga')
    form_class = MascotaForm
    success_url = reverse_lazy('mascotas:carga')
    success_message = "Mascota creada correctamente"
    permission_required = 'mascotas.add_mascota'
    login_url = reverse_lazy('usuarios:login')




class BorrarMascota(PermissionRequiredMixin,DeleteView):
    queryset = Mascota.objects.all()
    success_url = reverse_lazy('mascotas:carga')
    template_name = 'mascotas/carga_admin.html'
    pk_url_kwarg = 'pk'
    permission_required = 'mascotas.delete_mascota'
    login_url = reverse_lazy('usuarios:login')
    success_message = "Mascota eliminada correctamente"


    def get(self, request, *args, **kwargs):
        self.delete(self, request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return redirect('mascotas:carga')


class ModificarMascota(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    '''Clase para modificar mascotas'''
    model = Mascota
    template_name = 'mascotas/modificar.html'
    form_class = MascotaForm
    pk_url_kwarg = 'pk'
    permission_required = 'mascotas.change_mascota'
    login_url = reverse_lazy('usuarios:login')
    success_url = reverse_lazy('mascotas:carga')
    success_message = "Mascota modificada correctamente"



class BuscarMascota(PermissionRequiredMixin,ListView):
    '''Clase para buscar mascotas'''
    model = Mascota
    template_name = 'mascotas/resultado_busqueda_mascotas.html'
    context_object_name = 'mascotas'
    permission_required = 'mascotas.view_mascota'
    login_url = reverse_lazy('usuarios:login')


    def get_queryset(self):
        '''Metodo para buscar mascotas'''
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('mirco_chip',None)
        if busqueda:
            return queryset.filter(micro_chip__contains=busqueda)
        else:
            return queryset



class MascotasAutocomplete(PermissionRequiredMixin,autocomplete.Select2QuerySetView):
    '''Clase para autocompletar mascotas'''
    permission_required = 'mascotas.add_mascota'
    login_url = reverse_lazy('usuarios:login')

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Mascota.objects.none()

        qs = Mascota.objects.all()

        if self.q:
            qs = qs.filter(micro_chip__istartswith=self.q)

        return qs


class MascotasByDniAutocomplete(PermissionRequiredMixin,autocomplete.Select2QuerySetView):
    '''Clase para autocompletar mascotas por dni'''
    permission_required = 'mascotas.add_mascota'
    login_url = reverse_lazy('usuarios:login')

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Mascota.objects.none()

        qs = Mascota.objects.all()

        if self.q:
            qs = qs.filter(duenio__dni=self.q)

        return qs

# HISTORIAL

class CrearHistorial(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    '''Clase para crear historiales'''
    template_name = 'mascotas/historial_medico_admin.html'
    success_url = reverse_lazy('mascotas:carga_historial')
    form_class = HistorialForm
    permission_required = 'mascotas.add_historialclinico'
    login_url = reverse_lazy('usuarios:login')
    success_message = "Historial creado correctamente"

class BorrarHistorialVew(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    '''Clase para eliminar historiales'''
    model = HistorialClinico
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('mascotas:buscar')
    success_message = "Historial eliminado correctamente"
    template_name = 'mascotas/carga_admin.html'
    permission_required = 'mascotas.delete_historialclinico'
    login_url = reverse_lazy('usuarios:login')

    def get(self, request, *args, **kwargs):
        self.delete(self, request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return redirect('mascotas:carga')


class EditarHistorialView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    '''Clase para modificar historiales'''
    model = HistorialClinico
    template_name = 'mascotas/historial_medico_admin.html'
    form_class = EditarHistorialForm
    pk_url_kwarg = 'pk'
    success_message = "Historial modificado correctamente"
    permission_required = 'mascotas.change_historialclinico'
    login_url = reverse_lazy('usuarios:login')
    success_url = reverse_lazy('mascotas:carga')

class ListarHistorialesView(PermissionRequiredMixin,SingleTableView):
    '''Clase para listar historiales de una mascota'''
    model = HistorialClinico
    template_name = 'mascotas/listado_historiales.html'
    table_class = HistorialTable
    permission_required = 'mascotas.change_historialclinico'
    login_url = reverse_lazy('usuarios:login')

    def get_queryset(self):
        '''Metodo para buscar mascotas'''
        queryset = super().get_queryset()
        busqueda = self.kwargs.get('pk',None)
        if busqueda:
            return queryset.filter(mascota__id=busqueda)
        else:
            return queryset



# VACUNAS
class CrearVacunaView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    '''Clase para crear vacunas'''
    template_name = 'mascotas/vacunas_admin.html'
    success_url = reverse_lazy('mascotas:carga')
    form_class = VacunaForm
    permission_required = 'mascotas.add_vacuna'
    login_url = reverse_lazy('usuarios:login')
    success_message = "Vacuna cargada correctamente"

class ListarVacunasView(PermissionRequiredMixin,SingleTableView):
    '''Clase para listar vacunas de una mascota'''
    model = Vacuna
    template_name = 'mascotas/listado_vacunas.html'
    context_object_name = 'vacunas'
    table_class = VacunaTable
    permission_required = 'mascotas.view_vacuna'
    login_url = reverse_lazy('usuarios:login')

    def get_queryset(self):
        '''Metodo para buscar mascotas'''
        queryset = super().get_queryset()
        busqueda = self.kwargs.get('pk')
        print(busqueda)
        if busqueda:
            return queryset.filter(mascota=busqueda)
        else:
            return queryset


class EditarVacunaView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    '''Clase para listar vacunas de una mascota'''
    model = Vacuna
    template_name = 'mascotas/vacunas_admin.html'
    form_class = EditarVacunaForm
    pk_url_kwarg = 'pk'
    permission_required = 'mascotas.change_vacuna'
    login_url = reverse_lazy('usuarios:login')
    success_url = reverse_lazy('mascotas:carga')
    success_message = "Vacuna modificada correctamente"


class BorrarVacunaView(PermissionRequiredMixin,SuccessMessageMixin,DeleteView):
    '''Clase para eliminar vacunas de una mascota'''
    model = Vacuna
    pk_url_kwarg = 'pk'
    success_message = "Vacuna eliminada correctamente"
    success_url = reverse_lazy('mascotas:carga')
    template_name = 'mascotas/vacunas_admin.html'
    permission_required = 'mascotas.delete_mascota'
    login_url = reverse_lazy('usuarios:login')

    def get(self, request, *args, **kwargs):
        self.delete(self, request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return redirect('mascotas:carga')


class MisMascotasView(PermissionRequiredMixin,ListView):
    '''Clase para listar las mascotas de un usuario'''
    model = Mascota
    template_name = 'vista_usuarios/mascotas_usuario.html'
    context_object_name = 'mascotas'
    permission_required = 'mascotas.view_mascota'
    login_url = reverse_lazy('usuarios:login')

    def get_queryset(self):
        '''Metodo para buscar mascotas'''
        queryset = super().get_queryset()
        busqueda = self.request.user
        if busqueda:
            return queryset.filter(duenio=busqueda)
        else:
            return queryset

class VacunasMisMascotasView(PermissionRequiredMixin,SingleTableView):
    '''Clase para listar las vacunas de las mascotas de un usuario'''
    model = Vacuna
    template_name = 'vista_usuarios/listado_vacunas.html'
    context_object_name = 'vacunas'
    permission_required = 'mascotas.view_vacuna'
    login_url = reverse_lazy('usuarios:login')
    table_class = VacunaTablePropietario

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(mascota__duenio=self.request.user)
        return queryset


class HistorialesMisMascotasView(PermissionRequiredMixin,SingleTableView):
    '''Clase para listar los historiales de las mascotas de un usuario'''
    model = HistorialClinico
    template_name = 'vista_usuarios/historial_usuario.html'
    permission_required = 'mascotas.view_historialclinico'
    login_url = reverse_lazy('usuarios:login')
    table_class = HistorialTablePropietario

    def get_queryset(self,**kwargs):
        queryset = super().get_queryset()
        queryset.filter(mascota__duenio=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mascota'] = Mascota.objects.get(duenio=self.request.user)
        return context
