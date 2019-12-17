from django.urls import path

from apps.libros.views import ListLibro, DetailLibro

urlpatterns = [
    path('api/v1.0/libros/', ListLibro.as_view()),
    path('api/v1.0/libros/<int:pk>', DetailLibro.as_view()),
    #path('', include('apps.prestamos.urls')),
]
