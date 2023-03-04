# Generated by Django 4.0.10 on 2023-03-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietario',
            name='modificado',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='veterinario',
            name='modificado',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='fecha_alta',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='veterinario',
            name='fecha_alta',
            field=models.DateField(auto_now_add=True),
        ),
    ]
