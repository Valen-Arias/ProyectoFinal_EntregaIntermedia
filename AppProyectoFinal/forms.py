from django import forms
from .models import Sala



class AgregarPelicula(forms.Form):

    titulo = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=50)
    duracion = forms.IntegerField()
    clasificacion = forms.CharField(max_length=50)
    idiomas = forms.CharField(max_length=100)


class AgregarCombo(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=200)
    precio = forms.IntegerField()


class AgregarSala(forms.ModelForm):


    class Meta:
        model = Sala
        fields = ('__all__')
        widgets = {
            'descripcion': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripción...',
                    'class': 'textarea-sala'
                }
            )
        }