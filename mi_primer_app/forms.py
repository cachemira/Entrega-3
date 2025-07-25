from django import forms
from .models import Libro

class CursoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    duracion_semanas = forms.IntegerField(min_value=1, initial=4)
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    activo = forms.BooleanField(required=False, initial=True)

class EstudianteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email= forms.EmailField()
    edad = forms.IntegerField(min_value=10, max_value=100)
    fecha_inscripcion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

# class LibroForm(forms.Form):
#     nombre = forms.CharField(max_length=50)
#     autor = forms.CharField(max_length=50, initial = "Desconocido")
#     año = forms.IntegerField()
#     editorial = forms.CharField(max_length=50)

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['Titulo', 'Autor', 'Descripcion']