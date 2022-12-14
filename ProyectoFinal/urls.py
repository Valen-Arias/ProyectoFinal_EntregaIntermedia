"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppProyectoFinal.views import agregarPelicula, agregarSala, cartelera, agregarCombo, mostrarCombos, mostrarSalas, agregarComplejo, mostrarComplejos, busquedaPelicula, buscarPelicula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar-pelicula', agregarPelicula, name="agregar_pelicula"),
    path('cartelera', cartelera, name="cartelera"),
    path('agregar-combo', agregarCombo, name="agregar_combo"),
    path('combos', mostrarCombos, name="combos"),
    path('agregar-sala', agregarSala, name="agregar_sala"),
    path('salas', mostrarSalas, name="salas"),
    path('agregar-complejo', agregarComplejo, name="agregar_complejo"),
    path('complejos', mostrarComplejos, name="complejos"),
    path('buscar-pelicula', busquedaPelicula, name="buscar_peli"),
    path('buscar', buscarPelicula, name="buscar"),
]
