# Generated by Django 4.0.10 on 2023-03-09 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.BigIntegerField()),
                ('telefono', models.BigIntegerField(null=True)),
                ('direccion', models.CharField(max_length=250)),
                ('localidad', models.CharField(max_length=150)),
                ('provincia', models.CharField(max_length=150)),
                ('codigo_postal', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('modificado', models.DateField(auto_now=True)),
                ('tipo_usuario', models.CharField(choices=[('propietario', 'Propietario'), ('veterinario', 'Veterinario'), ('administrador', 'Administrador')], max_length=100)),
                ('observaciones', models.TextField(blank=True, max_length=500, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]