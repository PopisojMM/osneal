from django.db import models
from mascotas.models import Mascota

# Create your models here.
class Turno(models.Model):
    TIPO_TURNO = (
        ('Veterinaria', 'Veterinaria'),
        ('Peluquería', 'Peluquería'),
    )
    mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE)
    descripcion_corta = models.CharField(max_length=250)
    descripcion = models.TextField()
    tipo_turno = models.CharField(max_length=250,choices=TIPO_TURNO)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

