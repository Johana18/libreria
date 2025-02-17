from django import forms
from apps.libros.models import Libro

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libro
		fields = ['nombre_libro', 'genero', 'autor', 'editorial', 'descripcion']