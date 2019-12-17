from django.urls import path

from apps.usuarios.views import ListUsuario, DetailUsuario

urlpatterns = [
    path('api/v1.0/usuarios/', ListUsuario.as_view(), name="lista_usuarios" ),
    path('api/v1.0/usuarios/<int:pk>', DetailUsuario.as_view(), name="detalle_usuarios" ),
    #path('', include('apps.prestamos.urls')),
]
