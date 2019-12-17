from django.shortcuts import render
from apps.usuario.models import Usuario
from apps.usuario.serializer import UsuarioSerializer
from res_framework.views import APIView
from res_framework.response import Response
from res_framework import status

# Create your views here.
class ListUsuario(APIView):
	def get(self,request):
	usuario = Usuario.object.all()
		if usuario:
			serializer = UsuarioSerializer(usuario, many=True)
			return Response(data=serializer.data,status=status.HTTP_200_ok)
		result = {'result' : 'Error, nno se encuentran datos en labase de datos.'}
		return Response(result,status=status.HTTP_204_NO_CONTENT)
	def post(self,request):
		serializer = UsuarioSerializer(data=request.data)
		if serializer.is_valid();
			serializer.save()
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)	
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DetailUsuario