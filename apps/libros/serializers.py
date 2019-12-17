from rest_framework import serializers
from apps.libros.models import Libro

class LibroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Libro
		fields = ('__all__')