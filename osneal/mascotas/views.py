from django.shortcuts import render
from django.views.generic import CreateView
from mascotas.models import Mascota, MascotaForm
from usuarios.models import Usuario
from django.urls import reverse_lazy
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
            mascota.duenio = Usuario.objects.get(dni=request.POST.get("dni"))
            mascota.save()
            return render(request,self.template_name,{'mensaje':'Mascota creada correctamente'})
        else:
            return render(request,self.template_name,{"form":form})