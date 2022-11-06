from django.shortcuts import render, redirect
from .models import Pelicula, Producto
from .forms import AgregarPelicula, AgregarCombo

# Create your views here.


# def pelicula(request, titulo, genero, duracion, clasificacion, idiomas, salas):
    
#     pelicula = Pelicula(titulo = titulo, genero = genero, duracion = duracion, clasificacion = clasificacion, idiomas = idiomas, salas = salas)
#     pelicula.save()

#     return render (request, "agragarpelicula.html")


def agregarPelicula(request):

    if request.method == 'POST':

        peliculaFormulario = AgregarPelicula(request.POST)

        print(peliculaFormulario)

        if peliculaFormulario.is_valid:

            informacion = peliculaFormulario.cleaned_data

            pelicula = Pelicula(titulo=informacion['titulo'], genero=informacion['genero'], duracion=informacion['duracion'], clasificacion=informacion['clasificacion'], idiomas=informacion['idiomas'])

            pelicula.save()

            return redirect ('cartelera')
    
    else:

        peliculaFormulario = AgregarPelicula()
    
    return render(request, "agregar_pelicula.html", {"peliculaFormulario":peliculaFormulario})




def cartelera(request):

    lista = Pelicula.objects.all()
    
    return render(request, "cartelera.html", {"lista_peliculas": lista})




def agregarCombo(request):

    if request.method == 'POST':

        comboFormulario = AgregarCombo(request.POST)

        print(comboFormulario)

        if comboFormulario.is_valid:

            informacion = comboFormulario.cleaned_data

            combo = Producto(nombre=informacion['nombre'], descripcion=informacion['descripcion'], precio=informacion['precio'])

            combo.save()

            return redirect ('combos')
    
    else:

        comboFormulario = AgregarCombo()
    
    return render(request, "agregar_combo.html", {"comboFormulario":comboFormulario})



def mostrarCombos(request):

    lista = Producto.objects.all()
    
    return render(request, "combos.html", {"lista_combos": lista})