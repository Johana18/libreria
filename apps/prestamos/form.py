from django import forms
from apps.prestamos.models import Prestamo

class PrestamoForm(forms.ModelForm):
	class Meta:
		model = Prestamo
		fields = ['fecha_salida', 'fecha_entrega', 'usuario', 'libro', 'devuelto', 'comentario']