from rest_framework import serializers
from apps.prestamo.models import Prestamo
from apps.usuario.serializers import UsuarioSerializer
from apps.libro.serializers import LibroSerializer

class PrestamoSerializer(serializers.ModelSerializer):
	usuario = UsuarioSerializer(read_online=True)
	libro = LibroSerializer(read_online=True)
	
	class Meta:
		model = Prestamo
		fields = ('__all__')