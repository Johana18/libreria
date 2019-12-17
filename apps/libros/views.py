from django.shortcuts import render, Http404
from apps.libros.models import Libro
from apps.libros.serializers import LibroSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ListLibro(APIView):
	def get(self, request):
		libro = Libro.objects.all()
		if libro:
			serializer = LibroSerializer(libro, many=True)
			return Response(data=serializer.data,status=status.HTTP_200_OK)
		result = {'result' : 'Error, no se encuentran datos en la base de datos.'}
		return Response(result,status=status.HTTP_204_NO_CONTENT)

	def post(self,request):
		serializer = LibroSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)	
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailLibro(APIView):
	#la clase userDetail recibe el objeto tipo APIView para el manejor de vistas basada en clases para hacer el crud
    def get_object(self, pk):
        #esta función busca el id del libro para poder hacer uso del mismo
        try:
            return Libro.objects.get(pk=pk)
            #en el try, intentamos recuperar el id del libro, si existe nos devuelve el id
        except Libro.DoesNotExist:
            #en el except, nos indica que el libro no existe y nos devuelve el error 404 del código de rest
            raise Http404
    
    def get(self, request, pk):
        #esta funcino nos sirve para poder ver todos los datos del objeto del libro por su id
        libro = self.get_object(pk)
        #la variable user, nos indica que busca el id del libro que está en la base de datos
        if libro:
            #si existe el libro nos almacena los datos del mismo en la variable serializer y con return response nos lo muestra en la pagina
            serialize = LibroSerializer(libro)
            return Response(data=serialize.data)
        reslibroult = {'result': 'Error, no se encuentra el libro en la base de datos.'}
        return Response(result)
        # sino se encuentra el libro nos manda el error de la variable result y nos los muestra con el return response
    
    def put(self, request, pk):
        #la funcion put nos sirve para actualizar los datos de un libro específico
        libro = self.get_object(pk)
        #con la variable user buscamos el id del libro
        serialize = LibroSerializer(usuario, data=request.data)
        #con la variable serialize le mandamos los datos que vamos a cambiar a nuestro libro
        if serialize.is_valid():
            #el if nos sirve para saber si son validos los datos que vamos a modificar
            serialize.save()
            #si son validos los guarda
            return Response(data=serialize.data, status=status.HTTP_200_OK)
            #nos retorna el json con los datos actualizados del Libro
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        #sino se actualizaron los datos nos manda el error 
    
    def delete(self, request, pk):
        #la funcion delete nos sirve para eliminar los datos del libro
        libro = self.get_object(pk)
        #la variable user nos sirve para buscar el libro por su id
        if libro:
            #la funcion if, nos sirve para saber si el libro está en la base de datos
            libro.delete()
            #si el libro está en la base de datos nos retorna el mensaje del result
            result = {'result': 'Libro eliminado'}
            return Response(result, status=status.HTTP_200_OK)
        result = {'result': 'Error, no existe el dato en el sistema, puede que se haya eliminado con anterioridad.'}
        return Response(result, status=status.HTTP_204_NO_CONTENT)
        #Si no hay datos nos manda el mensaje de resualt con el codigo 204 del codigo REST