from django.db import models

from apps.usuarios.models import Usuario
from apps.libros.models import Libro
# Create your models here.


class Prestamo(models.Model):
	fecha_salida = models.DateTimeField(blank=True, null=True)
	fecha_entrega = models.DateTimeField(blank=True, null=True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
	devuelto = models.BooleanField(default=False)
	comentario =  models.TextField(blank=True, null=True)

	def __str__(self):
		return 'Prestamo # ' + self.id