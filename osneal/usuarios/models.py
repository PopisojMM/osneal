from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone

# Create your models here.


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser,PermissionsMixin):
    """
    Modelo de usuario para la aplicación.
    """
    TIPO_USUARIO = (
        ('propietario', 'Propietario'),
        ('veterinario', 'Veterinario'),
        ('administrador', 'Administrador'),
    )

    nombre= models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField("Correo electrónico", blank=True, unique=True)
    date_joined = models.DateTimeField("Fecha de login", default=timezone.now)

    objects = UsuarioManager()

    dni = models.CharField(max_length=20,null=True, blank=True,default=None)
    telefono = models.BigIntegerField(null=True)
    direccion = models.CharField(max_length=250,null=True, blank=True)
    localidad = models.CharField(max_length=150,null=True, blank=True)
    provincia = models.CharField(max_length=150,null=True, blank=True)
    codigo_postal = models.CharField(max_length=100,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    modificado = models.DateField(auto_now=True)
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=100)
    observaciones = models.TextField(max_length=500,null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

