# Generated by Django 4.0.10 on 2023-04-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_is_active_alter_usuario_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
