from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.
	class Usuario(AbstractUser):
		edad = models.IntegerField(blank=True, null=True)

		SEXO_CHOICE = (
		('F', 'Femenino'),
		('M', 'Masculino'),
		)
		sexo = models.CharField(max_length=1, choices=SEXO_CHOICE, blank=True, null=True)
		telefono = models.CharField(max_length=10, help_text="9611234567",blank=True, null=True)
		domicilio = models.TextField(blank=True, null=True)

		created_at = models.DateTimeField(auto_now_add=True)
		updated_at = models.DateTimeField(auto_now=True)

	#	def save(self, request= False, *args, **kwargs):
	#		if not self.pk:
	#			self.password = make_password(self.password)
	#		super(User, self).save(*args,**kwargs)


		def __str__(self):
			return self.first_name + ' ' + self.last_name + ' ' + self.username