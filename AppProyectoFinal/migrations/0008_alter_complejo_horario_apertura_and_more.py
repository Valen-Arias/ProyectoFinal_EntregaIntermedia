# Generated by Django 4.1.2 on 2022-11-18 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoFinal', '0007_remove_complejo_hora_apertura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complejo',
            name='horario_apertura',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='complejo',
            name='horario_cierre',
            field=models.TimeField(null=True),
        ),
    ]