from django.db import models
from usuarios.models import Usuario
from django.utils import timezone

class Mascota(models.Model):
    '''Clase para las mascotas'''
    OPCIONES_SEXO=(
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    )

    OPCIONES_TIPO_PLAN=(
        ('Plan Base', 'Plan Base'),
        ('Plan Estándar', 'Plan Estándar'),
        ('Plan Premium', 'Plan Premium'),
    )

    duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    micro_chip = models.CharField(max_length=250,unique=True)
    especie = models.CharField(max_length=250)
    raza = models.CharField(max_length=250)
    pelaje = models.CharField( blank=True, null=True,max_length=250)
    fecha_nacimiento = models.DateField(null=True)
    tipo_plan = models.CharField(max_length=250, choices=OPCIONES_TIPO_PLAN,default='Plan Base')
    # genero = models.CharField(max_length=10, choices=OPCIONES_SEXO,null=True, blank=True)
    # color = models.CharField(max_length=50, null=True, blank=True)
    # descripcion = models.TextField(null=True, blank=True)
    fecha_ingreso = models.DateField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateField(auto_now=True)
    fecha_baja = models.DateField(null=True)
    activo = models.BooleanField(default=True)
    edad = models.IntegerField(blank=True, null=True)

    def calcular_edad(self):
        '''Metodo para calcular la edad de la mascota'''
        if  self.fecha_nacimiento:
            hoy = timezone.now().date()
            edad = hoy.year - self.fecha_nacimiento.year
            if hoy < timezone.datetime(hoy.year, self.fecha_nacimiento.month, self.fecha_nacimiento.day).date():
                edad -= 1
            self.edad =  edad
    
    def save(self, *args, **kwargs):
        '''Metodo para guardar la edad de la mascota'''
        self.calcular_edad()
        super(Mascota, self).save(*args, **kwargs)


class Vacuna(models.Model):
    '''Clase para las vacunas'''
    TIPO_VACUNA=(
        ('Antirrábica', 'Antirrábica'),
        ('Puppy', 'Puppy'),
        ('Quintuple', 'Quintuple'),
        ('Sextuple', 'Sextuple'),
        ('Antitetánica', 'Antitetánica'),
        ('Mixomatosis', 'Mixomatosis'),
    )

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    tipo_vacuna = models.CharField(max_length=250, choices=TIPO_VACUNA)
    fecha_vacuna = models.DateField(null=True)
    fecha_proxima_vacuna = models.DateField(null=True)
    nro_vacuna = models.CharField(max_length=250,null=True,blank=True)



class HistorialClinico(models.Model):
    '''Clase para el historial clinico'''
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_historial = models.DateField(null=True)
    diagnostico = models.CharField(null=True, blank=False,max_length=250)
    tratamiento = models.TextField(null=True, blank=True)