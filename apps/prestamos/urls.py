from django.urls import path
from apps.prestamos.views import ListPrestamo, DetailPrestamo

urlpatterns = [
    path('api/v1.0/prestamos/', ListPrestamo.as_view(), name="list-prestamo" ),
    path('api/v1.0/prestamos/<int:pk>/', DetailPrestamo.as_view(), name="detail-prestamo"),
]
