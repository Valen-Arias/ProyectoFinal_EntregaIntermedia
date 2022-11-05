from django import forms



class AgregarPelicula(forms.Form):

    titulo = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=50)
    duracion = forms.IntegerField()
    clasificacion = forms.CharField(max_length=50)
    idiomas = forms.CharField(max_length=100)