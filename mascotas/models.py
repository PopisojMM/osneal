from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm
from django import forms

class Mascota(models.Model):
    duenio = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    raza = models.CharField(max_length=250,null=True)
    pelaje = models.CharField(max_length=250,null=True)
    edad = models.IntegerField(default=0,null=True)
    num_microchip = models.IntegerField(default=0)
    descripcion = models.TextField(max_length=5000,null=True,blank=True)

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - Dueño: {self.duenio.get_full_name()}'

class FormularioMascota(ModelForm):
    class Meta:
        model=Mascota
        fields = '__all__'

class Vacuna(models.Model):
    vacunas = models.ManyToManyField(Mascota)
    fecha = models.DateTimeField(auto_now_add=True,null=True)
    tipo = models.CharField(max_length=150,null=True)
    nombre_vacuna = models.CharField(max_length=150,null=True)
    proxima_dosis = models.DateTimeField(null=True)
    descripcion = models.TextField(max_length=5000,null=True,blank=True)
    lote = models.CharField(max_length=150,null=True)


class Turno(models.Model):
    mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE)
    fecha_turno =  models.DateTimeField()
    descripcion = models.TextField(max_length=5000,null=True,blank=True)

    def __str__(self) -> str:
        fecha_turno = timezone.localtime(self.fecha_turno)
        hora_turno = fecha_turno.strftime('%H:%M:%S')
        return f'Turno de: {self.mascota.nombre} - Hora: {hora_turno}'