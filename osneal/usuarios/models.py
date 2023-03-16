from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PerfilUsuario(models.Model):
    '''Modelo para los propietarios de los animales:
    se hereda de la clase User de Django'''
    
    TIPO_USUARIO = (
        ('propietario', 'Propietario'),
        ('veterinario', 'Veterinario'),
        ('administrador', 'Administrador'),
    )
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.BigIntegerField()
    telefono = models.BigIntegerField(null=True)
    direccion = models.CharField(max_length=250)
    localidad = models.CharField(max_length=150)
    provincia = models.CharField(max_length=150)
    codigo_postal = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    modificado = models.DateField(auto_now=True)
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=100)
    observaciones = models.TextField(max_length=500,null=True, blank=True)

    def __str__(self):
        return self.usuario.username
