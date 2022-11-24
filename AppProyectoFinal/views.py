from django.shortcuts import redirect, render

from .forms import AgregarCombo, AgregarPelicula, AgregarSala, AgregarComplejo
from .models import Pelicula, Producto, Sala, Complejo

# Create your views here.




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



def busqueda_pelicula(request):
    
    return render(request, "cartelera.html")




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



def agregarSala(request):


    if request.method == 'POST':

        salaFormulario = AgregarSala(request.POST)

        print(salaFormulario)

        if salaFormulario.is_valid:

            informacion = salaFormulario.cleaned_data

            sala = Sala(nombre=informacion['nombre'], descripcion=informacion['descripcion'])

            sala.save()

            return redirect ('salas')
    
    else:

        salaFormulario = AgregarSala()
    
    return render(request, "agregar_sala.html", {"salaFormulario":salaFormulario})


def mostrarSalas(request):

    lista = Sala.objects.all()
    
    return render(request, "salas.html", {"lista_salas": lista})




def agregarComplejo(request):


    if request.method == 'POST':

        complejoFormulario = AgregarComplejo(request.POST)

        print(complejoFormulario)

        if complejoFormulario.is_valid:

            informacion = complejoFormulario.cleaned_data

            complejo = Complejo(nombre=informacion['nombre'], direccion=informacion['direccion'], horario_apertura=informacion['horario_apertura'], horario_cierre=informacion['horario_cierre'])

            complejo.save()

            return redirect ('complejos')
    
    else:

        complejoFormulario = AgregarComplejo()
    
    return render(request, "agregar_complejo.html", {"complejoFormulario":complejoFormulario})




def mostrarComplejos(request):

    lista = Complejo.objects.all()
    
    return render(request, "complejos.html", {"lista_complejos": lista})


def busquedaPelicula(request):

    return render(request, "busquedapelicula.html")



def buscarPelicula(request):
    try:

        busqueda = request.GET['pelicula']

        peli = Pelicula.objects.get(titulo = busqueda)

        print(peli.titulo)
        print(type(peli))

        return render(request, "resultadoBusqueda.html", {'peli': peli, 'titulo': busqueda})

    except:
        return render(request, "error.html")