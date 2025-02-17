from rest_framework import serializers
from apps.prestamos.models import Prestamo
from apps.usuarios.serializers import UsuarioSerializer
from apps.libros.serializers import LibroSerializer

class PrestamoSerializer(serializers.ModelSerializer):
	usuario = UsuarioSerializer(read_only=True)
	libro = LibroSerializer(read_only=True)
	
	class Meta:
		model = Prestamo
		fields = ('__all__')