# Generated by Django 4.1.2 on 2022-11-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyectoFinal', '0003_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=750)),
            ],
        ),
    ]
