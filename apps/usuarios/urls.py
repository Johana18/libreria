from django.urls import path

from apps.usuarios.views import ListUsuario, DetailUsuario

urlpatterns = [
    path('api/v1.0/usuarios/', ListUsuario.as_view()),
    path('api/v1.0/usuarios/<int:pk>', DetailUsuario.as_view()),
    #path('', include('apps.prestamos.urls')),
]
