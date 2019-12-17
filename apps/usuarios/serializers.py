from rest_framework import serializers
from apps.usuarios.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ('__all__')