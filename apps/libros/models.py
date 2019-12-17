from django.db import models


# Create your models here.
class Libro(models.Model):
	GENERO_LIBRO = (
		('NO', 'Novela'),
		('CI', 'Ciencia'),
		('RO', 'Romance'),
		('CU', 'Cuentos'),
		('PO', 'Poesia'),
		('RE', 'Relato'),
	)
	nombre_libro =  models.CharField(max_length=50, blank=True, null=True)
	genero = models.CharField(max_length=2, choices=GENERO_LIBRO)
	autor = models.CharField(max_length=20, blank=True, null=True)
	editorial = models.CharField(max_length=20, blank=True, null=True)
	descripcion = models.TextField(blank=True, null=True)
	
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nombre_libro

