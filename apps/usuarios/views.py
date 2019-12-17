from django.shortcuts import render, Http404
from apps.usuarios.models import Usuario
from apps.usuarios.serializers import UsuarioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ListUsuario(APIView):
	def get(self, request):
		usuario = Usuario.objects.all()
		if usuario:
			serializer = UsuarioSerializer(usuario, many=True)
			return Response(data=serializer.data,status=status.HTTP_200_OK)
		result = {'result' : 'Error, no se encuentran datos en la base de datos.'}
		return Response(result,status=status.HTTP_204_NO_CONTENT)

	def post(self,request):
		serializer = UsuarioSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)	
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailUsuario(APIView):
	#la clase userDetail recibe el objeto tipo APIView para el manejor de vistas basada en clases para hacer el crud
    def get_object(self, pk):
        #esta función busca el id del usuario para poder hacer uso del mismo
        try:
            return Usuario.objects.get(pk=pk)
            #en el try, intentamos recuperar el id del usuario, si existe nos devuelve el id
        except Usuario.DoesNotExist:
            #en el except, nos indica que el usuario no existe y nos devuelve el error 404 del código de rest
            raise Http404
    
    def get(self, request, pk):
        #esta funcino nos sirve para poder ver todos los datos del objeto del usuario por su id
        usuario = self.get_object(pk)
        #la variable user, nos indica que busca el id del usuario que está en la base de datos
        if usuario:
            #si existe el usuario nos almacena los datos del mismo en la variable serializer y con return response nos lo muestra en la pagina
            serialize = UsuarioSerializer(usuario)
            return Response(data=serialize.data)
        result = {'result': 'Error, no se encuentra el usuario en la base de datos.'}
        return Response(result)
        # sino se encuentra el usuario nos manda el error de la variable result y nos los muestra con el return response
    
    def put(self, request, pk):
        #la funcion put nos sirve para actualizar los datos de un usuario específico
        usuario = self.get_object(pk)
        #con la variable user buscamos el id del usuario
        serialize = UsuarioSerializer(usuario, data=request.data)
        #con la variable serialize le mandamos los datos que vamos a cambiar a nuestro usuario
        if serialize.is_valid():
            #el if nos sirve para saber si son validos los datos que vamos a modificar
            serialize.save()
            #si son validos los guarda
            return Response(data=serialize.data, status=status.HTTP_200_OK)
            #nos retorna el json con los datos actualizados del usuario
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        #sino se actualizaron los datos nos manda el error 
    
    def delete(self, request, pk):
        #la funcion delete nos sirve para eliminar los datos del usuario
        usuario = self.get_object(pk)
        #la variable user nos sirve para buscar el usuario por su id
        if usuario:
            #la funcion if, nos sirve para saber si el usuario está en la base de datos
            usuario.delete()
            #si el usuario está en la base de datos nos retorna el mensaje del result
            result = {'result': 'Usuario eliminado'}
            return Response(result, status=status.HTTP_200_OK)
        result = {'result': 'Error, no existe el dato en el sistema, puede que se haya eliminado con anterioridad.'}
        return Response(result, status=status.HTTP_204_NO_CONTENT)
        #Si no hay datos nos manda el mensaje de resualt con el codigo 204 del codigo REST