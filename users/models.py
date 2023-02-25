from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    '''
    Modelo perfil, se relaciona a uno con modelo usurio de Django que ya tiene los campos
    first_name, last_name, email, etc..
    '''
    PROVINCIAS=[
        ('CH','CHACO'),
        ('CR','CORRIENTES'),
        ('MS','MISIONES'),
    ]

    LOCALIDADES = [
        ('RES','RESISTENCIA'),
        ('BAR','BARRANQUERAS'),
        ('FON','FONTANA'),
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dni = models.IntegerField(null=False)
    provincia = models.CharField(choices=PROVINCIAS,default='CH',max_length=3)
    localidad = models.CharField(choices=LOCALIDADES,default='RES',max_length=3)
    direccion = models.CharField(max_length=150)
    tel = models.CharField(max_length=20)
    

    class Meta:
        verbose_name='Perfil'
        verbose_name_plural='Perfiles'