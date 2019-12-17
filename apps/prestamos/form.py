from django import forms
from apps.prestamo.models import Prestamo

class PrestamoForm(forms.ModelForm):
	class Meta:
		model = Prestamo
		fields = ['fecha_salida', 'fecha_entrega', 'usuario', 'libro', 'devuelto', 'comentario']