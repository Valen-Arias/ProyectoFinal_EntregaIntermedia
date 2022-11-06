from django.db import models

# Create your models here.


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    duracion = models.IntegerField()
    clasificacion = models.CharField(max_length=50)
    idiomas = models.CharField(max_length=100)


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
