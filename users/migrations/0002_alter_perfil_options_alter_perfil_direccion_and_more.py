# Generated by Django 4.0.6 on 2023-02-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AlterField(
            model_name='perfil',
            name='direccion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tel',
            field=models.CharField(max_length=20),
        ),
    ]
