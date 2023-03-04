from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Propietario(models.Model):
    '''Modelo para los propietarios de los animales:
    se hereda de la clase User de Django'''
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    dni = models.BigIntegerField()
    telefono = models.BigIntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=250)
    localidad = models.CharField(max_length=150)
    provincia = models.CharField(max_length=150)
    codigo_postal = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    modificado = models.DateField(auto_now=True)
    observaciones = models.TextField(max_length=500)

    def __str__(self):
        return self.usuario.username
    
class Veterinario(models.Model):
    '''Modelo para los veterinarios:
    se hereda de la clase User de Django'''
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    dni = models.BigIntegerField()
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=250)
    localidad = models.CharField(max_length=150)
    provincia = models.CharField(max_length=150)
    codigo_postal = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    modificado = models.DateField(auto_now=True)
    matricula = models.CharField(max_length=50)
    observaciones = models.TextField(max_length=500)

    def __str__(self):
        return self.usuario.username
