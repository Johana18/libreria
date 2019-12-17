from django import forms
from apps.usuario.models import Usuario

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ['username', 'first_name', 'last_name', 'email', 'edad', 'sexo', 'telefono', 'domicilio']
		