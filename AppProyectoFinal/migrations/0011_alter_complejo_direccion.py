# Generated by Django 4.1.2 on 2022-11-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoFinal', '0010_complejo_horario_apertura_complejo_horario_cierre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complejo',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
    ]
