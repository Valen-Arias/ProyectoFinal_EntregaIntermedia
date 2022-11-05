from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import AgregarPelicula

# Create your views here.


# def pelicula(request, titulo, genero, duracion, clasificacion, idiomas, salas):
    
#     pelicula = Pelicula(titulo = titulo, genero = genero, duracion = duracion, clasificacion = clasificacion, idiomas = idiomas, salas = salas)
#     pelicula.save()

#     return render (request, "agragarpelicula.html")


def agregarPelicula(request):

    if request.method == 'POST':

        miFormulario = AgregarPelicula(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            pelicula = Pelicula(titulo=informacion['titulo'], genero=informacion['genero'], duracion=informacion['duracion'], clasificacion=informacion['clasificacion'], idiomas=informacion['idiomas'])

            pelicula.save()

            return redirect ('cartelera')
    
    else:

        miFormulario = AgregarPelicula()
    
    return render(request, "agregar_pelicula.html", {"miFormulario":miFormulario})


def cartelera(request):

    lista = Pelicula.objects.all()
    
    return render(request, "cartelera.html", {"lista_peliculas": lista})